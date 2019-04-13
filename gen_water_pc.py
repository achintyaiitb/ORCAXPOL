import subprocess
def gen_water_pc (i):# generates point charge file for ith water mol.
  f = open('uracil_Q.xyz','r')
  string = f.read().strip()
  f.close()
  f = open('pc_water'+str(i)+'.pc','r')
  l = f.readline().strip()#reads first line which contains no. of charges
  s = str(int(l)+12)+'\n'
  s += string+'\n'
  s += f.read().strip()#reads from the second line
  f.close()
  f = open('Water'+str(i)+'.pc','w')
  f.write(s)
  f.close()
  return

#gen_water_pc (2)


