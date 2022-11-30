# Python

## Compiling Binary Executables

```bash
pip install pyinstaller
pyinstaller --onefile $FILE
```

## Conda

###### Installation
```bash
conda update conda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

###### Environment Management
```bash
conda create --name $NAME python=$VERSION
conda remove --name $NAME --all
```

## Install Local Packages
```bash
pip install --no-build-isolation --no-deps --editable $PKG_ROOT_DIR
```
