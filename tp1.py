jumbled_superheroes = [ 'DocToR_sTRAngE',
'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

indices=[]
for index in enumerate(jumbled_superheroes):
    indices.append(index)
    
decoded_names=[names.replace("_"," ").lower() for names in jumbled_superheroes]

lamda=[]
for n in jumbled_superheroes:
    lamda.append(len(n))

name_lengths=list(map(len,decoded_names))

decoded_names.sort(key=lambda x: len(x))

formatted_list=[name.title() for name in decoded_names]

for i,name  in enumerate(formatted_list):
    print(f"{i+1}.{name}")

