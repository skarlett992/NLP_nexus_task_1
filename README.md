# Simple OCR reader with TessaractOCR

## Annotaion

Create a command‐line tool to do OCR and extract text from a given scanned document image.
### Input
Scanned document images ( include English only ). Your command needs to accept the following file formats.
PNG JPEG PDF
### Output
Extracted texts as a text file.

## Install
0. Configure venv ([link to manual](https://docs.python.org/3/tutorial/venv.html))  
1. Install project requirements `pip install -r /path/to/requirements.txt`
2. Put the image that you need to recognize into input directory


## Example of usage
0. Open cli-console and run command: `python main.py --input input/2003.00744v1_image_pdf.pdf --output output.txt`
1. See result into "output" directory

## Requirements
Python 3.7.7
```buildoutcfg
asgiref==3.4.1
backports.entry-points-selectable==1.1.0
CacheControl==0.12.6
cachy==0.3.0
certifi==2021.5.30
cfgv==3.3.1
charset-normalizer==2.0.5
cleo==0.8.1
click==8.0.1
clikit==0.6.2
crashtest==0.3.1
cycler==0.10.0
distlib==0.3.2
Django==3.2.7
filelock==3.0.12
html5lib==1.1
identify==2.2.14
idna==3.2
image==1.5.33
imageio==2.9.0
importlib-metadata @ file:///Users/yuriybiznigaev/Library/Caches/pypoetry/artifacts/58/de/f6/e8fb35077ed9c776f61299a35e9a8b8add9c0eb7be76880a7d80bf40dd/importlib_metadata-4.8.1-py3-none-any.whl
isort==5.9.3
joblib==1.0.1
keyring==21.8.0
kiwisolver==1.3.2
langid==1.1.6
lockfile==0.12.2
matplotlib==3.4.3
msgpack==1.0.2
nameparser==1.0.6
networkx==2.6.3
nltk==3.6.2
nodeenv==1.6.0
numpy==1.21.2
opencv-python==4.5.3.56
packaging==20.9
pandas==1.3.3
pastel==0.2.1
pdf2image==1.16.0
pexpect==4.8.0
Pillow==8.3.2
pkginfo==1.7.1
platformdirs==2.3.0
poetry==1.1.8
poetry-core==1.0.4
pre-commit==2.15.0
ptyprocess==0.7.0
pycountry==20.7.3
pylev==1.4.0
pyparsing==2.4.7
pytesseract==0.3.8
python-dateutil==2.8.2
pytz==2021.1
PyWavelets==1.1.1
PyYAML==5.4.1
regex==2021.8.28
requests==2.26.0
requests-toolbelt==0.9.1
scikit-image==0.18.3
scipy==1.7.1
shellingham==1.4.0
six==1.16.0
sqlparse==0.4.2
tifffile==2021.8.30
toml==0.10.2
tomlkit==0.7.2
tqdm==4.62.2
typing-extensions==3.10.0.2
urllib3==1.26.6
virtualenv==20.7.2
webencodings==0.5.1
yapf==0.31.0
zipp==3.5.0
```