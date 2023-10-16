# Prerequisites
Python and PIP installed on your system

## Git
To download the latest source from the Git server, do this:

```bash
git clone https://github.com/raktim707/Sortify.git
```
(you will get a directory named Sortify created, filled with the source code)

## Installation
Go to Sortify folder on terminal and run the following command to install"

``bash
pip install .
``

## How to use:
usage: sortify.py [-h] [-s SOURCE] [-d DEST] [-f {image,video,music,sheet,pdf,doc}]

What the program does

options:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        source path (This is the folder that you want to organize)
  -d DEST, --dest DEST  destination path (This is the folder where you want to move the files)
  -f {image,video,music,sheet,pdf,doc}, --file {image,video,music,sheet,pdf,doc}
                        file type (The type of file you want to move from source to destination folder)