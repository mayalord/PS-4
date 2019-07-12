import os 
import re
import string

def language(file_name):
    with open (file_name) as file_object:
        contents = file_object.read()
    
    sp = contents.split()
    
    List = []
    
    for words in sp:
        x = words.lower().strip("[¿􏰈|©􏰃􏰆􏰇!@#$%^&*()-_=+,.;:?/<>'`􏰁' []?]")
        List.append(x)
    
    
    counts = {}
    for word in List:
        if  not word in counts:
            counts[word] =0
        counts[word] += 1
    
    sorted_counts = sorted(counts.items(), key = lambda kv: kv[1], reverse = True)
    
    most_frequent = dict(sorted_counts[:11])
    
    for word in most_frequent.keys():
        most_frequent[word] = most_frequent[word]/len(List)
    
    return most_frequent


language('schloemp-tolle-koffer_DE.txt')
        
        
print("The most frequent words in German are ", language("schloemp-tolle-koffer_DE.txt"))
print("The most frequent words in English are ", language("eaton-boy-scouts_EN.txt"))
print("The most frequent words in Spanish are ", language("cherbonnel-mi-tio_SP.txt"))
print("The most frequent words in unknown language", language("unknown-lang.txt"))


german = language("schloemp-tolle-koffer_DE.txt")
unknown = language("unknown-lang.txt")
english = language("eaton-boy-scouts_EN.txt")
spanish = language("cherbonnel-mi-tio_SP.txt")




s=0
j=0
b=0

for w in unknown.keys():
    e2 = english.get(w, 0)
    u2 = unknown.get(w, 0)
    diff = abs(e2 - u2)
    s = s + diff
    
print("The difference between English and unknown is " +  str(s))

for w in unknown.keys():
    s2 = spanish.get(w, 0)
    u2 = unknown.get(w, 0)
    diff_1 = abs(s2 - u2)
    b = b + diff_1
    
print("The difference between Spanish and unknown is " + str(b))

for w in unknown.keys():
    g2 = german.get(w, 0)
    u2 = unknown.get(w, 0)
    diff_2 = abs(g2 - u2)
    j = j + diff_2
#   
print("The difference between German and unknown is " + str(j))


if s < j and s < b:
   print('The unknown language is English') 

elif j < s and j < b:
    print('The unknown language is German') 

else: 
    print('The unknown language is Spanish')
        
   
    