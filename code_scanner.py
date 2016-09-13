#!/usr/bin/env python

import os, sys

haystack_dir = sys.argv[1]
needles_file = sys.argv[2]


# inserts all needles into a list
needles = []
f = open(needles_file)
for line in f.readlines():
	# excludes the \n
	needles.append(line[0:-1])
f.close()

needle_total = len(needles)
cur_dir = os.getcwd()
needle_count = 0
output = ""


# begin haystack search
for needle in needles:
	needle_count = needle_count + 1
	print "searching needle " + str(needle_count) + " of " + str(needle_total)
	os.system("grep -r -c \"" + needle + "\" " + haystack_dir + " > " + cur_dir + "/found")
	potential = 0
	total_found = 0
	file_matches = ""
	f = open(cur_dir + "/found")
	for line in f.readlines():
		potential = int(line.split(':')[-1])
		total_found = total_found + potential
		if potential > 0:
			file_matches = file_matches + line
	f.close()
	output = output + "needle " + str(needle) + " found " + str(total_found) + " times\n"
	output = output + file_matches + "\n"

print output
