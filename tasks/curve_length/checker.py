import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
parser.add_argument('answer', type=str)
args = parser.parse_args()

with open(args.output, 'r') as f:
    outp = f.readline().strip()
with open(args.answer, 'r') as f:
    ans = f.readline().strip()

try:
    if ans == outp:
        print('OK')
        quit(0)
    else:
        print('WA')
        quit(1)
except Exception as e:
    print('PE')
    quit(2)
