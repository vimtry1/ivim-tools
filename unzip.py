import argparse
import zipfile

parser = argparse.ArgumentParser(description='Unzip for iVim')
parser.add_argument('infile', help='Target zip file')
parser.add_argument('outfile', help='Output file or directory path')
args = parser.parse_args()

with zipfile.ZipFile(args.infile) as f:
    f.extractall(args.outfile)
