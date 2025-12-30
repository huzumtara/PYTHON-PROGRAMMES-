#displaying the vowels and consonants using the while loop 
word="Thundersoft"
vowels="a,e,i,o,u"
vowels_list[]
consonant_list[]
i=0
    while i< len(word):
        ch=word[i].lower()
        if ch in vowels:
            vowels_list.append(ch)
        else:
            consonant_list.append(ch)
        i+=1
     print("out")   
