#!/usr/bin/env python
import subprocess

file_types = ["doc","docx","pdf"]
source = "~/Documents/workspace/mac_backup_script"
dest = "~/Dropbox/scratch/backup_test"

files = []
for ft in file_types:
    if not(subprocess.call("find %s/*.%s"%(source,ft),shell=True)): files.extend(subprocess.check_output("find %s/*.%s"%(source,ft),shell=True).split("\n")[:-1])
for f in files: subprocess.check_output("rsync -a %s %s/"%(f,dest),shell=True)