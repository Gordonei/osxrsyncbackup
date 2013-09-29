#!/usr/bin/env python
import subprocess

file_types = ["doc","docx"]
source = "~/Documents"
dest = "~/Dropbox/backup"

files = []
for ft in file_types:
    if not(subprocess.call("find %s -name *.%s"%(source,ft),shell=True)): files.extend(subprocess.check_output("find %s -name *.%s"%(source,ft),shell=True).split("\n")[:-1])
for f in files:
	if("\'" in f):
		subprocess.check_output("rsync -a \"%s\" %s/"%(f,dest),shell=True)
	else: 
		subprocess.check_output("rsync -a \'%s\' %s/"%(f,dest),shell=True)
