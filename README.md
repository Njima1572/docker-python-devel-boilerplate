# Python docker boilerplate with poetry

## Project initialization

```bash
./bin/build
./bin poetry init
```

## Add script

`./bin/run` is a script that runs the main function in `app/__main__.py` by using `poery script`, you can customize it to run any script you want, but here is the sample snippet to add to your `pyproject.toml`

```
[tool.poetry.scripts]
main = "app.__main__:main"
```

## Recommendation
Use direnv to add the `bin` directory to your path.
