PYTHON ?= python3

## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <TARGETS> ...\033[0m\n\n\033[1mTargets:\033[0m\n\n"
	@sed -n 's/^##//p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/ /'

## api_generate: Generate API client code.
# HACK: pythonのdatetimeは0年を表現できないので replace "default: '0000-01-01T00:00:00.000000Z'" -> "default: '0001-01-01T00:00:00.000000Z'"
# HACK2: Makefileが生成されないので手動でコピーしてる
.PHONY: api_generate
api_generate: write-version
	mkdir -p tmp
	curl -o tmp/v3-api.yaml https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml
	sed -i -e "s/0000-01-01T00:00:00.000000Z/0001-01-01T00:00:00.000000Z/g" tmp/v3-api.yaml
	poetry run openapi-python-client generate \
		--path tmp/v3-api.yaml \
		--output-path libs/aiotraq \
		--custom-template-path=templates/aiotraq \
		--config api-client-config.yaml
	cp templates/aiotraq/Makefile.jinja libs/aiotraq/Makefile
	cp LICENSE libs/aiotraq/LICENSE
	rm -rf tmp
	cd libs/aiotraq && poetry install

## api_update: Generate API client code.
# HACK: pythonのdatetimeは0年を表現できないので replace "default: '0000-01-01T00:00:00.000000Z'" -> "default: '0001-01-01T00:00:00.000000Z'"
# HACK2: Makefileが生成されないので手動でコピーしてる
.PHONY: api_update
api_update: write-version
	mkdir -p tmp
	curl -o tmp/v3-api.yaml https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml
	sed -i -e "s/0000-01-01T00:00:00.000000Z/0001-01-01T00:00:00.000000Z/g" tmp/v3-api.yaml
	poetry run openapi-python-client generate \
		--path tmp/v3-api.yaml \
		--output-path libs/aiotraq \
		--custom-template-path=templates/aiotraq \
		--config api-client-config.yaml \
		--overwrite
	cp templates/aiotraq/Makefile.jinja libs/aiotraq/Makefile
	cp LICENSE libs/aiotraq/LICENSE
	rm -rf tmp
	cd libs/aiotraq && poetry install


## lint: Lint and type-check packages using the root development environment.
.PHONY: lint
lint:
	@runtime_python=$$(poetry run python -c 'import sys; print(sys.executable)'); \
	for project in libs/aiotraq libs/bot libs/message; do \
		(cd $$project && "$$runtime_python" -m ruff check . && "$$runtime_python" -m mypy .) || exit $$?; \
	done


## write-version: Sync versions from root metadata (or VERSION=0.3.0).
.PHONY: write-version
write-version:
	$(PYTHON) scripts/version.py $(VERSION)

## check-version: Check package and generator version consistency.
.PHONY: check-version
check-version:
	$(PYTHON) scripts/version.py --check

## test: Run runtime regression tests with installed packages.
.PHONY: test
test:
	poetry run python -m unittest discover -s tests -v
