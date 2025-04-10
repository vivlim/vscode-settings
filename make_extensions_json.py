#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml"
# ]
# ///

# Create a .vscode/extensions.json using extensions from a profile
# That file's structure is { "recommendations": ["extension.id"] }

import argparse
import pathlib
script_path = pathlib.Path(__file__)
script_name = script_path.stem
parser = argparse.ArgumentParser(prog=script_name, description='generates extensions.py for vscode')
parser.add_argument('filename', help="extensions.yaml file to read")
args = parser.parse_args()

source = pathlib.Path(args.filename)
if not source.exists():
    raise Exception(f"File {source} doesn't exist")

import yaml

recommendations = []
extensions_json = {'recommendations': recommendations}

with source.open() as stream:
    source_data = yaml.safe_load(stream)
    for extension in source_data['enabled']:
        recommendations.append(extension['id'])

(script_path.parent / '.vscode').mkdir(exist_ok=True)
destination = script_path.parent / '.vscode' / 'extensions.json'
import json

with destination.open(mode='wt') as stream:
    stream.write(json.dumps(extensions_json, indent=2))

print(f'Created {destination} with {len(recommendations)} extensions')
