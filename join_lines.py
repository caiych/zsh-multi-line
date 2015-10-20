#! /usr/bin/python

import sys
sys.stdout.write(' '.join(sys.stdin.read().split('\\\n')))
