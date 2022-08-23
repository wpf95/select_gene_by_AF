## -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:46:42 2022

@author: Wangpf
"""
import sys
import re

fo = open(sys.argv[1], "r")  ##cat all chrom AF result as input file
fo1 = open(sys.argv[2], "r")  ##your genome gff file 
fo2 = open(sys.argv[3], "w")  ##out file conclude pos gene name

list = []
list1 = []
for line in fo1:
    if line.startswith("#"):
        pass
    else:
        line = line.strip().split("\t")
        list.append(line)
# fo2.write(list)
for i in list:
    if i[2] == "CDS":
        for m in i[8].split(";"):
            re1 = r'gene=[A-Za-z0-9]+'
            gene = re.findall(re1, m)
            if gene != []:
                list1.append(i[0:1] + i[3:4] + i[4:5] + gene + i[2:3])
                # fo2.write(list1)
pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25, pos26, pos27, pos28, pos29 = [
    [] for i in range(29)]
d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29 = [
    {} for i in range(29)]

for j in list1:
    chrom = j[0]
    if chrom == str(1):
        pos1.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(2):
        pos2.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(3):
        pos3.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(4):
        pos4.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(5):
        pos5.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(6):
        pos6.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(7):
        pos7.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(8):
        pos8.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(9):
        pos9.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(10):
        pos10.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(11):
        pos11.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(12):
        pos12.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(13):
        pos13.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(14):
        pos14.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(15):
        pos15.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(17):
        pos17.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(18):
        pos18.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(19):
        pos19.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(20):
        pos20.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(21):
        pos21.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(22):
        pos22.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(23):
        pos23.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(24):
        pos24.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(25):
        pos25.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(26):
        pos26.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(27):
        pos27.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(28):
        pos28.append([j[1], j[2], j[3], j[4]])
    elif chrom == str(29):
        pos29.append([j[1], j[2], j[3], j[4]])

d1[1] = pos1
d2[2] = pos2
d3[3] = pos3
d4[4] = pos4
d5[5] = pos5
d6[6] = pos6
d7[7] = pos7
d8[8] = pos8
d9[9] = pos9
d10[10] = pos10
d11[11] = pos11
d12[12] = pos12
d13[13] = pos13
d14[14] = pos14
d15[15] = pos15
d16[16] = pos16
d17[17] = pos17
d18[18] = pos18
d19[19] = pos19
d20[20] = pos20
d21[21] = pos21
d22[22] = pos22
d23[23] = pos23
d24[24] = pos24
d25[25] = pos25
d26[26] = pos26
d27[27] = pos27
d28[28] = pos28
d29[29] = pos29

d = {**d1, **d2, **d3, **d4, **d5, **d6, **d7, **d8, **d9, **d10, **d11, **d12, **d13, **d14, **d15, **d16, **d17,
     **d18, **d19, **d20, **d21, **d22, **d23, **d24, **d25, **d26, **d27, **d28, **d29}

list2 = []
list3 = []
for m in fo:
    list2.append(m.strip().split())
for n in list2:
    if n[0] == str(1):
        for line3 in d[1]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(2):
        for line3 in d[2]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(3):
        for line3 in d[3]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(4):
        for line3 in d[4]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(5):
        for line3 in d[5]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(6):
        for line3 in d[6]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(7):
        for line3 in d[7]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(8):
        for line3 in d[8]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(9):
        for line3 in d[9]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(10):
        for line3 in d[10]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(11):
        for line3 in d[11]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(12):
        for line3 in d[12]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(13):
        for line3 in d[13]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(14):
        for line3 in d[14]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(15):
        for line3 in d[15]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(16):
        for line3 in d[16]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(17):
        for line3 in d[17]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(18):
        for line3 in d[18]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(19):
        for line3 in d[19]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(20):
        for line3 in d[20]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(21):
        for line3 in d[21]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(22):
        for line3 in d[22]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(23):
        for line3 in d[23]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(24):
        for line3 in d[24]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(25):
        for line3 in d[25]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(26):
        for line3 in d[26]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(27):
        for line3 in d[27]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(28):
        for line3 in d[28]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")
                list3.append(line3[0])
    elif n[0] == str(29):
        for line3 in d[29]:
            if int(n[1]) > int(line3[0]) and int(n[1]) < int(line3[1]):
                fo2.write(n[0] + "\t" + n[1] + "\t" + "[" + line3[0] + " "+line3[1] + "]" + "\t" + str(line3[2]).lstrip(
                    "gene=") + "\t" + line3[3] + "\n")



