## -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:46:42 2022

@author: Wangpf
"""

fo = open(r"E:\heatmap\head.list3", "r") #genotype file，i use phase file
fo1 = open(r"E:heatmap\list1.txt", "r")  #alt list，it put your alt name list
fo2 = open(r"E:\heatmap\list2.txt", "r")  #ref list ， it put your ref name list

m = 0
n = 0

num1 = 60
num2 = 34

list = []
list1=[]
list2=[]

## 找位置信息
for line in fo:
    if line.startswith("##"):
        pass
    elif line.startswith("#"):
        line = str(line).strip("\n").split("\t")
        #print(line)
        for p in line:
            n = n + 1
            l = (str(p) + "\t" + str(n)).split("\t")
            list.append(l)
    else:
        line = str(line).strip("\n").split("\t")
        for l1 in fo1:
            l1 = l1.strip("\n")
            for h in list:
                if l1 == h[0]:
                    list1.append(h[1])
        for l2 in fo2:
            l2 = l2.strip("\n")
            for k in list:
                if l2 == k[0]:
                    list2.append(k[1])

list3=[]
list4=[]
for i in list1:
    list3.append("line"+"["+str(int(i)-1)+":"+str(i)+"]")
print(str(list3).rstrip("]").lstrip("[").replace(",","+").replace("'",""))

for j in list2:
    list4.append("line"+"["+str(int(j)-1)+":"+str(j)+"]")
print(str(list4).rstrip("]").lstrip("[").replace(",","+").replace("'",""))


##two print result used to input change select_gene_gz.py 








        




