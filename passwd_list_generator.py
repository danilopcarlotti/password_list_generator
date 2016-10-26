import re
from itertools import permutations

##common separators of words and symbols

separators = ["@","-","?","_","*","%","!","#"]

##substitution dictionary: words for symbols/numbers

substitution_dictionary = {"a":"@","e":"3","s":"5","i":"1","s":"$","s":"§","e":"&","o":"0"}

##main list for pentesting.

passwd_list = open("passwd_list.txt","a",encoding='utf-8')

##lists that store important names and dates for the subject

names = [n for n in input("Type important names for the subject separated by space. Ex.: relatives, pet, favorite series, etc...\n").split(" ")]
dates = [d for d in input("Type relevant dates for the subject in the following format MMDDYYYY or DDMMYYYY. Ex.: aniversary, birthday, etc...\n").split(" ")]
names2 = []
dates2 = []

def add_names(names_list):
    for n in names_list:
        for i in range(10):
            passwd_list.write(n+str(i)+"\n")
            for s in separators:
                passwd_list.write(n+str(s)+str(i)+"\n")
            for j in range(10):
                passwd_list.write(n+str(i)+str(j)+"\n")
                for q in separators:
                    passwd_list.write(n+str(q)+str(i)+str(j)+"\n")
                for k in range(10):
                    passwd_list.write(n+str(i)+str(j)+str(k)+"\n")
                    for r in separators:
                        passwd_list.write(n+str(r)+str(i)+str(j)+str(k)+"\n")
                    for l in range(10):
                        passwd_list.write(n+str(i)+str(j)+str(k)+str(l)+"\n")
                        for t in separators:
                            passwd_list.write(n+str(t)+str(i)+str(j)+str(k)+str(l)+"\n")

for d in dates:
    for l in d:
        dates2.append(l)

for i in range(4,9):
    for p in permutations(dates2,i):
        passwd_list.write("".join(p)+"\n")


for n in names:
    for s in substitution_dictionary:
        aux = re.sub(s,substitution_dictionary[s],n)
        if aux not in names2:
            names2.append(aux)

add_names(names)
add_names(names2)

passwd_list.close()