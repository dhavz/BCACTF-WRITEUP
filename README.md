# BCACTF-WRITEUP



Challenge -->>>  Large-Data

In this challange we upto 2700 text file in 27 different folder so we have to do some analysis technique to extract the flag.

![Screenshot_2019-06-17 BCACTF(1)](https://user-images.githubusercontent.com/42002820/59654705-12153a80-91b5-11e9-9aeb-0ed4892cb612.png)


As we can see in above challenge they given a link to download that files for analysis. and they clearly told that flag is 27 character long.

At first i have open file from a folder and get some random characters. that are in every files.then i decided to do something with the characters to extract the flag. so i'm doing trial on one file i have design a solver for one file that read data from file then make sum of each characters ASCII value and finally take average by from counting character emmmmmm... the equation like

####  flagChar = SUM_OF_ALL_CHARACTER(ASCII_CODE)/TOTAL_CHARACTERS_OF_FILE
  
by doing this i got flags characters like bcactf{.............. then i have created a solver that do this stuff in each file and folder..

## SOLVER.py
------------------------------------------------------------  

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


By running this solver we got 100 Flags--->
![flags](https://user-images.githubusercontent.com/42002820/59613123-f7eb4600-913b-11e9-9765-30502175cafc.png)

100 flags link -->
https://raw.githubusercontent.com/dhavz/BCACTF-WRITEUP/master/flags


So after that i have found a flag from that list that have good meaningful words like a FLAGGG!!!!!!!!!!!!

## bcactf{crunch1ng_num5_c00l}

c001_dh@\/7_
