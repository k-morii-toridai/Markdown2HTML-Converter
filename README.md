# Markdown2HTML-Converter

## Refs

https://pypi.org/project/Markdown/

## Execution log (On MacOS)

- Create a virtual environment

```zsh
python3 -m venv FileManipulatorProgam
```

- Activate virtual enviroment

```zsh
source bin/activate
```

- Deactivate virtual environment

```zsh
deactivate
```

- Install a library

```zsh
pip3 install markdown
```

- For confirmation

```zsh
pip3 list
```

stdout:

```
Package  Version
-------- -------
Markdown 3.7
pip      24.0
```

- Convert .md to .html file

```shell
python3 file-converter.py markdown inputfile outputfile
```

-- inputfile: .md ファイルへのパス
-- outputfile: プログラムを実行後に作成される.html

sample-case:

```zsh
python3 file-converter.py markdown sample.md sample.html
```
