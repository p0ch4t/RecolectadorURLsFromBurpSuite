"""
Python script that converts Burp Suite HTTP proxy history files to CSV or HTML files
"""
from __future__ import unicode_literals
from __future__ import print_function

import sys
import argparse
import base64

import xmltodict
from backports import csv

def main():
    args = parse_arguments()
    http_history = parse_http_history(args.filename)
    convert_to_output_file(http_history)


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', help='Burp Suite HTTP proxy history file')
    return parser.parse_args()


def convert_to_output_file(http_history):
        for line in http_history['items']['item']:
            #print(line['method']+' '+line['url']+line['path'])
            print(line['url']+line['path'])

def parse_http_history(filename):
    with open(filename, 'rb') as f:
        return xmltodict.parse(f)


def base64decode(line):
    decoded = base64.b64decode(line)
    replace = 'backslashreplace' if sys.version_info[0] >= 3 else 'replace'
    return decoded.decode('UTF-8', errors=replace)

if __name__ == '__main__':
    # In python 3, unicode is renamed to str
    if sys.version_info[0] >= 3:
      unicode = str
    main()
