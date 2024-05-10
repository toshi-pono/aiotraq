## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <TARGETS> ...\033[0m\n\n\033[1mTargets:\033[0m\n\n"
	@sed -n 's/^##//p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/ /'

## api_generate: Generate API client code.
.PHONY: api_generate
api_generate:
	cd libs && poetry run openapi-python-client generate \
		--url https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml \
		--custom-template-path=../templates/aiotraq \
		--config ../api-client-config.yaml

## api_update: Generate API client code.
.PHONY: api_update
api_update:
	cd libs && poetry run openapi-python-client update \
		--url https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml \
		--custom-template-path=../templates/aiotraq \
		--config ../api-client-config.yaml
