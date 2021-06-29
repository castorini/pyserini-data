import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True, help="input dir")
parser.add_argument('--output', type=str, required=True, help="output dir")
args = parser.parse_args()

if not os.path.exists(args.output):
    os.mkdir(args.output)
df = pd.read_pickle(os.path.join(args.input, 'embedding.pkl'))
df.to_pickle(os.path.join(args.output, 'embedding.pkl'), protocol=4)
