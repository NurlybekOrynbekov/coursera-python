import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
key = args.key
val = args.val

dictionary = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if(os.path.exists(storage_path)):
    with open(storage_path, 'r') as f:
        dictionary = json.loads(f.read())

if key is not None and val is not None:
    with open(storage_path, 'w') as f:
        if key in dictionary:
            dictionary[key].append(val)
        else:
            dictionary[key] = [val, ]
        f.write(json.dumps(dictionary))
elif key is not None:
    if key in dictionary:
        print(', '.join(dictionary[key]))
    else:
        print('')