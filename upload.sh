rm -r dist
poetry run python -m build
poetry run twine upload dist/* --verbose