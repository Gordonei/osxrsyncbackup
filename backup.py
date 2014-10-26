#!/usr/bin/env python
import subprocess

file_types = ["doc"]
max_size = 1024*1024*50

source = "~"
dest = "~/Dropbox/scratch/backup_test"

for fs in file_types:
    subprocess.call("rsync -auvm --max-size=%d --include=\"*/\" --include=\"*.%s\" --exclude=\"*\" %s %s"%(max_size,fs,source,dest),shell=True)