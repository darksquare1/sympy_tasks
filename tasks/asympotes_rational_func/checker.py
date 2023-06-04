import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
parser.add_argument('answer', type=str)
args = parser.parse_args()

with open(args.output, 'r') as f:
    outp = []
    outp.append(f.readline().strip().replace(' ', ''))
    outp.append(f.readline().strip().replace(' ', ''))
with open(args.answer, 'r') as f:
    ans = []
    ans.append(f.readline().strip().replace(' ', ''))
    ans.append(f.readline().strip().replace(' ', ''))
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
