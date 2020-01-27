import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Plugin Remove for iVim')
parser.add_argument('plugin_name', help='The plugin name of removing. eg. "xxx/yyy.vim"')
args = parser.parse_args()

# Set plugin directories
PLUGDIRNAME = args.plugin_name.split("/")[1] + '-master'
PACKDIR = os.environ['HOME'] + '/.vim/pack/'
CUSTOMDIRNAME = os.listdir(PACKDIR)[0]
STARTDIR = PACKDIR + CUSTOMDIRNAME + '/start/'
OPTDIR = PACKDIR + CUSTOMDIRNAME + '/opt/'
NOTFOUND = False

if os.path.isdir(STARTDIR + PLUGDIRNAME):
    shutil.rmtree(STARTDIR + PLUGDIRNAME)
    print(f'Plugin removed "{args.plugin_name}".')
elif os.path.isdir(OPTDIR + PLUGDIRNAME):
    shutil.rmtree(OPTDIR+ PLUGDIRNAME)
    print(f'Plugin removed "{args.plugin_name}".')
else:
    print(f'Plugin was not founded.')
