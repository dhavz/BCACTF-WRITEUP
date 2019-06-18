import os
f = []
root = os.getcwd()
i=0
for filename in os.listdir(os.getcwd()):
     f.append(filename)

f.pop()
f1=[]
for i in range(0, len(f)): 
    f[i] = int(f[i])
f.sort()
flag=[]

st = ""
for i in f:
      os.chdir(os.getcwd()+"\\"+str(i))
      filelist = os.listdir(os.getcwd())
      cntch=0
      charcode=0
      i=0
      for j in range(0, len(filelist)): 
          filelist[j] = int(filelist[j])
      filelist.sort()
      
      for afile in filelist:
            if(i<100):
                  #print(afile)
                  fp = open(str(afile),"r")
                  for filedata in fp:
                        for ch in filedata:
                              charcode += ord(ch)
                              cntch = cntch + 1 
                  st += (chr(int(charcode/cntch)))
                  cntch=0
                  charcode=0
            i+=1
      
      flag.append(st)
      os.chdir(root)
      st=""
print(len(flag))
k=0
l=0
flags=""
for i in range(0,100):
     for j in range(0,27):
               flags += flag[k][l]
               k=k+1
     l=l+1
     print(flags)
     flags=""
     k=0
