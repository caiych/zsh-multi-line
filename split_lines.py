#! /usr/bin/python

import sys

raw = sys.stdin.read()

tokens = raw.split(' ')

splitted = []
last = 0
for token in tokens:
  if last + len(token) > 80:
    splitted.append('\\\n')
    last = 0

  last += len(token)
  splitted.append(token)

sys.stdout.write(' '.join(splitted))

