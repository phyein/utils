# Python

## Style Guide
https://peps.python.org/pep-0008

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
conda install python=$VERSION
```

###### Upgrading
```bash
conda update --all
pip install --update $PACKAGE
pip freeze --local |sed -rn 's/^([^=# \t\\][^ \t=]*)=.*/echo; echo Processing \1 ...; pip install -U \1/p' |sh
```

## Install Local Packages
```bash
pip install --no-build-isolation --no-deps --editable $PKG_ROOT_DIR
```

## Compiling Binary Executables

```bash
pip install pyinstaller
pyinstaller --onefile $FILE
```
