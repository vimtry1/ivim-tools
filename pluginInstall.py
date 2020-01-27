from urllib.request import urlretrieve
import argparse
import os
import ssl
import shutil
import zipfile

parser = argparse.ArgumentParser(description='Plugin Installer for iVim')
parser.add_argument('plugin_name', help='The plugin name of installing. eg. "xxx/yyy.vim"')
parser.add_argument('--opt', action='store_true', help='Install for option directory')
args = parser.parse_args()

# Download zip file from github.com
URL = f'https://codeload.github.com/{args.plugin_name}/zip/master'
TMPDIR = os.environ['TMPDIR']
DLFILE = TMPDIR + 'master.zip'
ssl._create_default_https_context = ssl._create_unverified_context
urlretrieve(URL, DLFILE)

# Unzip 
UNZIPDIR = TMPDIR + 'master/'
with zipfile.ZipFile(DLFILE) as f:
    f.extractall(UNZIPDIR)

# Copy plugin files to iVim plugin directory
PLUGDIRNAME = os.listdir(UNZIPDIR)[0]
PACKDIR = os.environ['HOME'] + '/.vim/pack/'
CUSTOMDIRNAME = os.listdir(PACKDIR)[0]

if args.opt:
    TARGET = PACKDIR + CUSTOMDIRNAME + '/opt/'
else:
    TARGET = PACKDIR + CUSTOMDIRNAME + '/start/'

if os.path.isdir(TARGET + PLUGDIRNAME):
    shutil.rmtree(TARGET + PLUGDIRNAME)

res = shutil.move(UNZIPDIR + PLUGDIRNAME, TARGET)
print(f'Plugin installed to "{res}".')

# Clean up temporary files
os.remove(DLFILE)
shutil.rmtree(UNZIPDIR)
