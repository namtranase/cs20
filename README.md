# CS20

Solve CS20 Assignment based on Tensoflow 1x.


# Installation guide


```
$ git clone https://github.com/namtranase/cs20
$ cd cs20

# Create the virtual environment python
python3 -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt

$ pre-commit install
```

## Currently used hooks:

- `isort`: Sort imports.
- `black`: General python formatter.
- `flake8`: Check PEP8 convention.
- `pre-commit`: Run those hooks before commits.

# Work Convention

- Code convention: Follow PEP8 convention (include docstrings for functions).
- Update `__init__.py` when you add new modules.
- Use pre-commit so that the code would not be messy when merge between commits:
  - Usually, you can just `git commit` and `pre-commit` will run itself.
  - If you want to run it manually, use `pre-commit run --all-files` to run all files, `pre-commit run <hook_id>` to run a specific hook.
- Remember to put understandable commit descriptions.
