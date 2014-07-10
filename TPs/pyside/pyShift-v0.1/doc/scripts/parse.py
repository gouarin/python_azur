import os

def readfile(filename):
    f=open(filename,'r')
    l=f.readlines()
    f.close()
    return l

def extractdoc(filename):
    r=[]
    for l in readfile(filename):
      if (l[:4]=='c ##'):
          r+=l[5:]
    return r

def writefile(fsource,fdest):
    if (os.path.exists(fsource)):
        l=extractdoc(fsource)
        f=open(fdest,'w')
        f.writelines(l)
        f.close()

if (__name__=='__main__'):
  import sys
  writefile(sys.argv[1],sys.argv[2])
