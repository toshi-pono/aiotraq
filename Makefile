## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <TARGETS> ...\033[0m\n\n\033[1mTargets:\033[0m\n\n"
	@sed -n 's/^##//p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/ /'

## api_generate: Generate API client code.
# HACK: pythonのdatetimeは0年を表現できないので replace "default: '0000-01-01T00:00:00.000000Z'" -> "default: '0001-01-01T00:00:00.000000Z'"
.PHONY: api_generate
api_generate:
	mkdir -p tmp
	curl -o tmp/v3-api.yaml https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml
	sed -i -e "s/default: '0000-01-01T00:00:00.000000Z'/default: '0001-01-01T00:00:00.000000Z'/g" tmp/v3-api.yaml
	cd libs && poetry run openapi-python-client update \
		--path ../tmp/v3-api.yaml \
		--custom-template-path=../templates/aiotraq \
		--config ../api-client-config.yaml
	rm -rf tmp

## api_update: Generate API client code.
# HACK: pythonのdatetimeは0年を表現できないので replace "default: '0000-01-01T00:00:00.000000Z'" -> "default: '0001-01-01T00:00:00.000000Z'"
.PHONY: api_update
api_update:
	mkdir -p tmp
	curl -o tmp/v3-api.yaml https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml
	sed -i -e "s/default: '0000-01-01T00:00:00.000000Z'/default: '0001-01-01T00:00:00.000000Z'/g" tmp/v3-api.yaml
	cd libs && poetry run openapi-python-client update \
		--path ../tmp/v3-api.yaml \
		--custom-template-path=../templates/aiotraq \
		--config ../api-client-config.yaml
	rm -rf tmp


## test: Run lint
.PHONY: lint_all
lint_all:
	poetry run ruff check .
	poetry run mypy .
	cd libs/aiotraq && poetry run ruff check .
	cd libs/aiotraq && poetry run mypy .
	cd libs/bot && poetry run ruff check .
	cd libs/bot && poetry run mypy .
	cd libs/message && poetry run ruff check .
	cd libs/message && poetry run mypy .
