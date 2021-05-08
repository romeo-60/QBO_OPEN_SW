#!/usr/bin/env python3
# -*- coding: latin-1 -*-
#--- software modified by Romeo Ceccato ---

import sys


FIFO_cmd = '/opt/qbo/pipes/pipe_cmd'


# scan stdin and send to pipe_cmd
if len(sys.argv) == 1:
	line = ""
	while 1:

		idx = 0

		print("Opening FIFO...")
		line = raw_input('QBO_>> ')

		with open(FIFO_cmd, 'w') as fifo:

			print("FIFO opened")
			print "line: ", line

			fifo.write(line)

			if line == "exit" or line == "quit":
				sys.exit()

			fifo.close()

sys.exit()
