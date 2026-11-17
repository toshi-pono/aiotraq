"""Exercise the patched generator and custom metadata without changing the shipped client."""

import compileall
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib


ROOT = Path(__file__).resolve().parents[1]


def main():
    # Quotes, backslashes and newlines must remain documentation, never executable code.
    description = 'Untrusted """ description \\ newline\nraise RuntimeError("injected")\n'
    schema = {
        "openapi": "3.0.3",
        "info": {"title": "Generator regression", "version": "1.0.0", "description": description},
        "paths": {
            "/files": {"post": {
                "operationId": "upload_file",
                "description": description,
                "requestBody": {"required": True, "content": {"multipart/form-data": {"schema": {
                    "$ref": "#/components/schemas/Upload"
                }}}},
                "responses": {"204": {"description": "Uploaded"}},
            }},
        },
        "components": {"schemas": {"Upload": {
            "type": "object", "description": description, "required": ["file", "name", "enabled"],
            "properties": {
                "file": {"type": "string", "format": "binary"},
                "name": {"type": "string", "description": description},
                "enabled": {"type": "boolean"},
            },
        }}},
    }
    with tempfile.TemporaryDirectory(prefix="aiotraq-generator-") as temp:
        folder = Path(temp)
        spec = folder / "schema.json"
        spec.write_text(json.dumps(schema))
        config = folder / "config.json"
        config.write_text(json.dumps({
            "project_name_override": "generator-smoke", "package_name_override": "generator_smoke",
            "package_version_override": "0.3.0", "post_hooks": [],
        }))
        output = folder / "generated"
        subprocess.run([
            sys.executable, "-m", "openapi_python_client", "generate", "--path", str(spec),
            "--config", str(config), "--output-path", str(output),
            "--custom-template-path", str(ROOT / "templates/aiotraq"), "--fail-on-warning",
        ], check=True)
        metadata = tomllib.loads((output / "pyproject.toml").read_text())
        assert metadata["tool"]["poetry"]["version"] == "0.3.0"
        assert metadata["tool"]["poetry"]["dependencies"]["python"] == ">=3.11,<4.0"
        assert compileall.compile_dir(output / "generator_smoke", quiet=1)
        # __version__ reads distribution metadata; provide minimal local metadata for this smoke package.
        dist_info = output / "generator_smoke-0.3.0.dist-info"
        dist_info.mkdir()
        (dist_info / "METADATA").write_text("Name: generator-smoke\nVersion: 0.3.0\n")
        subprocess.run([sys.executable, "-c", """
from io import BytesIO
from generator_smoke.models.upload import Upload
from generator_smoke.types import File
from generator_smoke.api.default.upload_file import _get_kwargs
body = Upload(file=File(payload=BytesIO(b'contents'), file_name='test.txt'), name='safe', enabled=True)
kwargs = _get_kwargs(body=body)
assert kwargs['method'] == 'post'
assert kwargs['url'] == '/files'
fields = dict(kwargs['files'])
assert fields['file'][0] == 'test.txt'
assert fields['file'][1].read() == b'contents'
assert fields['name'][1] == b'safe'
"""], cwd=output, env={**os.environ, "PYTHONPATH": str(output)}, check=True)
    print("Generator escaping, metadata, imports and multipart upload checks passed.")


if __name__ == "__main__":
    main()
