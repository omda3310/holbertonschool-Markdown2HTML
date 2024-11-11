#!/usr/bin/python3
"""The Markdown file"""

import sys
import os
import hashlib


def md5_hash(text):
    """md5 parsing"""

    return hashlib.md5(text.encode()).hexdigest()


def process_line(line):
    """Heading parsing"""

    if line.startswith("#"):
        level = len(line.split()[0])
        content = line[level + 1:].strip()
        return f"<h{level}>{content}</h{level}>"

    line = line.replace("**", "<b>").replace("__", "<em>")

    if "[[" in line and "]]" in line:
        text = line.split("[[")[1].split("]]")[0]
        line = line.replace(f"[[{text}]]", md5_hash(text))

    if "((" in line and "))" in line:
        text = line.split("((")[1].split("))")[0]
        modified_text = text.replace('c', '').replace('C', '')
        line = line.replace(f"(({text}))", modified_text)

    return line


def main():
    """test function"""

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(process_line(line) + "\n")


if __name__ == "__main__":
    main()
