punctuations = '''.,?!:;'"'''
whole_analize=input('give me input')
list_of_punctuations=list(punctuations)
print(list_of_punctuations)
for i in list_of_punctuations:
        whole_analize=whole_analize.replace(i,'')
print(whole_analize)