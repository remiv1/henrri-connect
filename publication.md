# Publication instructions

```bash
python -m build
twine check dist/*
twine upload dist/*
```

## Mettre à jour la documentation

```bash
cd documentation/sphinxdoc/
make html
cp -r _build/html/* ../docs/
```
