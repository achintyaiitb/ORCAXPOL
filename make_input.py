def make_input(coord,pc):#enter coords file and pc file
  s = '! RHF def2-SVP  def2/J RIJCOSX\n\n'
  s += '%pointcharges "'+pc+'"\n\n'
  s += '* xyz 0 1\n\n'
  f = open(coord,'r')
  s += f.read()
  f.close()
  s += '\n*\n'
  L = coord.split('.')
  name = L[0]+'_pc.inp'
  f = open(name,'w')
  f.write(s)
  f.close()
  return

#make_input ('uracil.xyz','uracil.pc')
 
