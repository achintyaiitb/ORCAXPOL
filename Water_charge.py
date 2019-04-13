'''from math import *
import sys,os
from pprint import pprint
import subprocess
import shutil
'''
def energy (filename):
 f = open (filename,'r')
 s = f.read()
 i = s.find('TOTAL SCF ENERGY')
 i = i + len('TOTAL SCF ENERGY') 
 j = i
 count = 0
 while True:
  if s[j] == '\n': count+=1
  if count == 3: break
  j+=1
 j+=1
 k = j
 while True:
  if s[k] == '\n':
    t = s[j:k]
    count+=1
    j=k+1
    u=t.split()
    f.close()
    return float(u[5]) #returns energy in eV 
    break
  k+=1

 
def charge (filename,n):
 f = open (filename,'r')
 s = f.read()
 i = s.find('MULLIKEN ATOMIC CHARGES')
 i = i + len('MULLIKEN ATOMIC CHARGES')
 j = i
 count = 0
 Q = []
 while True:
  if s[j] == '\n': count+=1
  if count == 2: break
  j+=1
 j+=1
 k = j
 while True:
  if s[k] == '\n':
    t = s[j:k]
    count+=1
    j = k+1
    u = t.split()
    Q.append(u[3])#Check ORCA output file to understand u[3] 
  k+=1
  if count == 2 + n: break#n is no. of atoms #Value of count has to be set depending on output file   
 return Q
   

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

def E(i,j): #i is the index of h2o molecule
 return energy('Water'+str(i)+'_'+str(j)+'.out')

#res = subprocess.check_output(["module", "load", "pbs"], shell=True)
#print (res) 
'''f = open ('temp_inp.inp','r')
string = ''
for l in f:
 string += l.strip()+'\n'

i = 0 #no.of H2O molecules 
k = 0

q1 = -1
q2 = +0.5
q3 = +0.5
epsilon = 0.01
n = 0# no. of water molecules

input_coord = 'Water2.xyz'#enter the filename of coordinates
with open(input_coord,'r') as coord:
 j = 0 #iteration no.
 while True:
   ##Put the energy convergence here
   ##If |E i j - E i j-1| > epsilon for any i then continue, else break 
   
   i = 0
   j+=1
   while True :
    i+=1
    k = 1
    if i == n : break
    coord =  open(input_coord,'r')
    f1 = open ('Water'+str(i)+'_'+str(j)+'.inp','a') #this can be extended to n input files
    f1.write(string.strip()+'\n')

    while True : # n is no. of water molecules; hence no. of inp files at each iter 
      
      line = coord.readline()
      line = line.strip()
      if line == '':
         n = k#n is no. of water molecules
         f1.write('*\n')
         break
      
      #f1 = open ('Water'+str(i)+'_'+str(j)+'.inp','a') #this can be extended to n input files
      #f1.write(string.strip()+'\n')   
      if i==k:
         f1.write(line.strip()+'\n')
         line = coord.readline()
         f1.write(line.strip()+'\n')
         line = coord.readline()
         f1.write(line.strip()+'\n')
      else:  #remember to change the q's
      
         line = line.replace('O    ','Q '+str(q1)) 
         f1.write(line.strip()+'\n')
         line = coord.readline()
         line = line.replace('H    ','Q '+str(q2))
         f1.write(line.strip()+'\n')
         line = coord.readline()
         line = line.replace('H    ','Q '+str(q3))
         f1.write(line.strip()+'\n')
      k+=1
      ##Open ORCA output file and change q1,q2,q3 for the next k (use i=k)
      if j==1: q1,q2,q3 = -1,0.5,0.5
      else:
       Q = charge ('Water'+str(i)+'_'+str(j-1)+'.out',2)#Use n; here n=2 for dimer
       q1 = Q[0]
       q2 = Q[1]
       q3 = Q[2]
    with open('Water'+str(i)+'_'+str(j)+'.inp', 'r') as fin:
     print fin.read()
    #submit('Water'+str(i)+'_'+str(j))
    coord.close()
   for m in range (i):
     if abs(E(m+1,j) - E(m+1,j-1)) > epsilon : continue
   break

#Q = charge ('Water2_RHF.out',2)
#print Q
'''
