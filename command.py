import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', action='store_true', help='Print "c"')
parser.add_argument('-d', action='store_true', help='Print "d"')
args = parser.parse_args()

if args.c:
    print('c')
elif args.d:
    print('d')
