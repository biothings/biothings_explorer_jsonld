import json
import yaml
import pandas as pd
import requests
from pathlib import Path

def int2str(d):
    """
    Iterrative function
    Convert all integer values in the dictionary/JSON to string


    Params
    ======
    d: (dict)
        dictionary to perform int2str function
    """
    for k, v in d.items():
        if isinstance(v, dict):
            int2str(v)
        elif isinstance(v, list):
            for _v in v:
                if isinstance(_v, dict):
                    int2str(_v)
        else:
            if type(v) == int:
                d.update({k: str(v)})

def readFile(file_path):
    """
    Given a file_path, return the file in json/xml/csv
    format based on the suffix

    Params
    ======
    file_path: (str)
        The file path could be a URL or a local file path
        The suffix of the path could be in csv or json or yaml
    """

    # First check if the url or local file path is valid
    # if url/local file is invalid, return empty
    if file_path.startswith('http'):
        status = requests.get(file_path).status_code
        if status == 200:
            data = requests.get(file_path).content
        else:
            print('The url "{}" is invalid!!!! Please double check!'.format(file_path))
            return
    else:
        if Path(file_path).is_file():
            with open(file_path) as f:
                data = f.read()
        else:
            print('The local file path "{}" is invalid!!! Please double check!'.format(file_path))
            return
    # handle csv file using pandas module
    if file_path.endswith('csv'):
        return pd.read_csv(file_path, encoding="ISO-8859-1")
    # handle yaml file using yaml module
    elif file_path.endswith('yml') or file_path.endswith('yaml'):
        return yaml.load(data)
    # handle json file using json module
    elif file_path.endswith('json'):
        if file_path.startswith('http'):
            return json.loads(data.decode())
        else:
            return json.loads(data)
    else:
        print("readFile function could not handle file format other than csv, yml or json!")
