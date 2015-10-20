#! /usr/bin/python
import os
location = os.path.abspath(os.curdir)

template = open('multi-line.zsh').read()
rendered = template.replace(r'%%location%%', location)

with open(os.path.expanduser('~/.zshrc'), 'a') as zshrc:
  zshrc.write(rendered)
