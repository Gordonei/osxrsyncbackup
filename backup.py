#!/usr/bin/env python
import subprocess

file_types = ["doc","docx","pdf"]
source = "~/Documents/workspace/mac_backup_script"
dest = "~/Dropbox/scratch/backup_test"

files = []
for ft in file_types: files.extend(subprocess.check_output("cd %s;find . | grep [A-Z]*\.%s$"%(source,ft),shell=True).split("\n")[:-1])
for f in files: subprocess.check_output("cd %s;rsync -Ravz %s %s"%(source,f,dest),shell=True)