#!/usr/bin/env python

import re
import argparse

def main():
    parser = create_parser()
    args = parser.parse_args()
    filename = str(args.filename)
    if filename == "None":
        parser.print_help()
    else:
        extract_emails(filename)

def extract_emails(file):
    file = open(file)
    file_contents = file.read()
    file.close()
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', file_contents)
    for email in emails:
        print email

    return emails

def create_parser():
    parser = argparse.ArgumentParser(description="Extract all emails from file")
    parser.add_argument("-f", dest="filename", help="path for the file")
    return parser

if __name__ == "__main__":
    main()
