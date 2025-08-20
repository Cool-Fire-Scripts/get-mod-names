# Copyright (c) 2025 Arthur Taft

import json
import argparse
import re
from pathlib import Path

# create parser to read command line arguments
parser = argparse.ArgumentParser(description='A script to parse json mod files')

# add arguments
parser.add_argument('--input', '-i', type=str, help='Path to input file')
parser.add_argument('--output', '-o', type=str, default='output.txt', help='Path to output file')

# read the arguments
args = parser.parse_args()

# set variables equal to the arguments
input_file_path = Path(args.input)
output_file_path = Path(args.output)

# set regex
mod_name = re.compile(r'(?<=mods/)(.*?\.jar)')

# read json file
json_data = json.loads(input_file_path.read_text(encoding="utf-8"))

# get mod filepaths
mod_file_paths = [
    item["path"] for item in json_data.get("files", [])
    if isinstance(item, dict) and isinstance(item.get("path"), str)
]

# get matches
matches = []
for match in mod_file_paths:
    matches.extend(mod_name.findall(match))

# write to file
output_file_path.write_text("\n".join(matches))
print(f"Saved {len(matches)} matches to {output_file_path}")