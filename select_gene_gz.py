## -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:46:42 2022

@author: Wangpf
"""

import sys
import gzip
fo=gzip.open(sys.argv[1],"r")  #input your genotype file
fo1=open(sys.argv[2],"w")   ##output AF
 
m=0
n=0

num=60
num2=34

list1=[]
list2=[]

for line  in fo:
    if line.startswith("#"):
        pass
    else:
        line = line.strip("\n").split("\t")
        for i in line[9:9+num]:  ##you need change here used first out print
            if i != "0|0":
                m = m +1
        list1.append(m)

        for j in line[9+num:]:   ##you need change here used first out print
            if j != "0|0":
                n = n+1
        list2.append(n)
        try:
            t1=list1[-1]-list1[-2]
            t2=list2[-1]-list2[-2]
            r1=t1/num
            r2=t2/num2
            print(r1)
            if r1 > 0.9 :
                fo1.write(line[0]+"\t"+line[1]+"\t"+str(r1)+"\t"+str(r2)+"\n")
        except:
            continue
fo.close()
fo1.close()


