# Contributing

Thanks for checking out this repository.

## Good Contributions

- provider compatibility fixes
- better retry and cooldown behavior
- more example clients
- Docker and deployment improvements
- docs that help developers get to a working request faster

## Before Opening A PR

1. run the test suite
2. keep changes focused
3. update docs if behavior changes
4. preserve upstream credit where relevant

## Local Setup

```bash
python -m pip install -e .[dev]
pytest -q
```
