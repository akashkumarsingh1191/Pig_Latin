message=input("Enter message to translate english to Latin: ")
message_list=message.split()
pig_latin=[]
vowel=('a','e','i','o','u')

for word in message_list:
    # print(word)
    prefix=""
    while(len(word) > 0 and not word[0].isalpha()):
        prefix+=word[0]
        word=word[1:]
        # print(word)
    if len(word)==0:
        pig_latin.append(prefix)
        continue
    #separating last letter from word "test123" remove 123
    suffix=""
    while not word[-1].isalpha():
        suffix+=word[-1]
        # print(suffix)
        word=word[:-1]
    suffix=suffix[::-1]
    print('suffix:{suffix}')
    was_upper=word.isupper()
    was_title=word.istitle()
    # print(was_upper,was_title,word)
    word=word.lower()
    # print(word)
    prefix_const=""
    if not word[0] in vowel:
        prefix_const+=word[0]
        word=word[1:]
    if prefix_const !="":
        word+=prefix_const+'ay'
    else:
        word+="yay"
    # print(word)
    if was_upper:
        word=word.upper()
    if was_title:
        word=word.title()
    pig_latin.append(prefix + word + suffix)
print(" ".join(pig_latin))