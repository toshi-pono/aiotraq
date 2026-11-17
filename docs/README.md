# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

Node.js 22 or newer is required. CI uses Node.js 22.

### Installation

```
$ npm ci
```

### Local Development

```
$ npm run start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Validation

```bash
npm run typecheck
npm run test:dependencies
npm run build
npm audit
```

Review the complete dependency tree, including build and development dependencies. Update compatible parent packages first; do not use `npm audit fix --force` to accept unrelated major changes or downgrades.

The withdrawn `deepmerge` advisory [GHSA-gcqx-w48m-w2h4](https://github.com/advisories/GHSA-gcqx-w48m-w2h4) does not describe a security vulnerability. It is not a reason to introduce an incompatible override. No audit suppression is configured for it.

### Temporary security overrides

Docusaurus 3.10.2 still constrains several transitive dependencies below their patched major versions. `package.json` applies overrides only beneath the affected parents:

| Parent | Patched dependency | Compatibility checked |
| --- | --- | --- |
| `@docusaurus/core` | `tinypool ^2.1.2` | Static rendering through the worker pool |
| `copy-webpack-plugin`, `css-minimizer-webpack-plugin` | `serialize-javascript ^7.1.3` | Production asset copying and CSS minimization |
| `sockjs` | `uuid ^11.1.1` | CommonJS `v4()` API used by SockJS |

These dependencies require newer Node.js versions; this site uses Node.js 22 or newer. Remove each override when its parent accepts the patched version, then rerun the complete validation commands. Do not replace them with a blanket audit ignore.

### Build

```
$ npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

This website is deployed on [GitHub Pages](https://pages.github.com/). The deployment is automated using GitHub Actions. The workflow file is located at `.github/workflows/deploy.yml`.
