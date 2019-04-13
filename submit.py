import subprocess
import sys,os
import shutil


def submit (filename):
 inp=filename+'.inp'
 out=filename+'.out'
 run_arg='~/orca/x86_exe/orca '+ inp+' > '+out
 print run_arg
 print run_arg
 with open(inp, 'r') as fin:
    print fin.read()
 print 'came here'
 res = subprocess.call([run_arg],shell=True)
 return# (shell == True)

