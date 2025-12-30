# displaying vowels and consonants
word= "Thundersoft"
vowels= "a,e,i,o,u"
vowels_list=[]
consonant_list=[]
for ch in word.lower():
    if ch in vowels:
        vowels_list.append(ch)
    else:
        consonant_list.append(ch)
print("word:", word)
print("vowels_list:", vowels_list)
print("consonant_list:",consonant_list)
