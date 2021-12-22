#!/usr/bin/env python

import sys
import crypt

if len(sys.argv) != 2:
  print("Please provide one argument: the plain-text password")
  exit()

password = sys.argv[1]

hash = crypt.crypt(password, crypt.METHOD_SHA512)

print(hash)