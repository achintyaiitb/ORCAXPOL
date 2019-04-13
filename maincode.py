import separate
import Water_charge
import charge_water
import pc_water
import sys,os
import subprocess
import shutil
import make_input
import replace_by_Q
import gen_water_pc
import gen_uracil_pc
import charge_water
import submit
import energy

N = input ("Enter the coordinates file: ")

n = separate.separate(N)

#replace_by_Q.replace_by_Q('uracil.xyz')

for i in range (n):
  charge_water.pointcharge('Water'+str(i+1)+'.xyz')

for i in range (n):
  pc_water.pc_water(i+1,n)

gen_uracil_pc.gen_uracil_pc(n)

#for i in range (n):
#  gen_water_pc.gen_water_pc(i+1)

make_input.make_input('uracil.xyz','uracil.pc')

#for i in range (n):
#  make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')

submit.submit('uracil_pc')

#for i in range (n):
#  submit.submit('Water'+str(i+1)+'_pc')


En = energy.energy('uracil_pc.out')

print En

replace_by_Q.replace_by_Q('uracil.xyz','uracil_pc.out')#update uracil charges from 1st iter

for i in range (n):
  gen_water_pc.gen_water_pc(i+1)#gen. pc files for water using updated uracil charges

for i in range (n):
  make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')

for i in range (n):
  submit.submit('Water'+str(i+1)+'_pc')



Eo = 0

epsilon = 0.0001
while (abs(Eo-En) >= epsilon):
  print abs(Eo-En)
  print 'Entered while'
  Eo = En
  replace_by_Q.replace_by_Q('uracil.xyz','uracil_pc.out')#update uracil charges
  for i in range(n):
    replace_by_Q.replace_by_Q('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'_pc.out')#update water charges
  for i in range (n):
    pc_water.pc_water(i+1,n)
  gen_uracil_pc.gen_uracil_pc(n)#gen. uracil pc file
  for i in range (n):
    gen_water_pc.gen_water_pc(i+1)#gen. water pc file

  make_input.make_input('uracil.xyz','uracil.pc')#make input files with updated charges
  for i in range (n):
    make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')
  
  submit.submit('uracil_pc')#submit input files
  for i in range (n):
    submit.submit('Water'+str(i+1)+'_pc')

  En = energy.energy('uracil_pc.out')
  print En

print 'Converged energy = '+str(En)



