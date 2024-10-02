message=input("Enter the message that want to change in Pig Latin: ")
input_list=message.split()
pig_latin=[]

vowel=('a','e','i','o','u')

def separate_prefix_suffix(p_word):
    prefix=""
    suffix=""
    while len(p_word)>0 and not p_word[0].isalpha():
        prefix+=p_word[0]
        p_word=p_word[1:]
    if len(p_word) == 0:
        return (prefix,suffix,p_word)
    while not p_word[-1].isalpha():
        suffix += p_word[-1]
        p_word=p_word[:-1]
    suffix=suffix[::-1]
    return (prefix,suffix,p_word)

def translate_piglatin(p_word):
    prefix_const=""
    if not p_word[0] in vowel:
        prefix_const += p_word[0]
        p_word=p_word[1:]
        if prefix_const != "":
            p_word+=prefix_const+'ay'
    else:
        p_word += 'yay'
    return p_word

for word in input_list:
    prefix,suffix,word=separate_prefix_suffix(word)
    if word == "":
        pig_latin.append(prefix)
        continue
    is_upper=word.isupper()
    is_title=word.istitle()
    word=word.lower()
    
    word=translate_piglatin(word)
    if is_upper:
        is_lower=word.upper()
    if is_title:
        is_lower=word.title()
    pig_latin.append(prefix + word + suffix)
print(" ".join(pig_latin))    