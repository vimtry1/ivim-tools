import argparse
import zipfile

parser = argparse.ArgumentParser(description='Zip for iVim')
parser.add_argument('infile', help='Target a file')
parser.add_argument('outfile', help='Output zip file')
args = parser.parse_args()

with zipfile.ZipFile(args.outfile, 'w', compression=zipfile.ZIP_DEFLATED) as f:
    f.write(args.infile, arcname=args.infile)
