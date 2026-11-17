PYTHON ?= python3

## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <TARGETS> ...\033[0m\n\n\033[1mTargets:\033[0m\n\n"
	@sed -n 's/^##//p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/ /'

## api_generate: Disabled on v0.2; generate on main and backport reviewed code.
## api_update: Disabled on v0.2; generate on main and backport reviewed code.
.PHONY: api_generate api_update
api_generate api_update:
	@echo "API generation is disabled on v0.2. Generate on main, then backport reviewed Python 3.8-compatible code."
	@exit 1


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
