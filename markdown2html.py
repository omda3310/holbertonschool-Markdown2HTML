#!/usr/bin/python3
"""The Markdown file"""

import sys
import os


def main():
    """Check if the number of arguments is less than 3
    (script name + 2 arguments)
    """

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)

    exit(0)


if __name__ == "__main__":
    main()
