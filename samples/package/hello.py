#!/usr/bin/env python

import sys

for path in sys.path:
    print(path)

from package.something import Something

def main():   
    print(Something.something())

if __name__ == "__main__":
    main()
