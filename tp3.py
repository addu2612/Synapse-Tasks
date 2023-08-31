
encoded_lists = [
[1, 2, 3, 4, 6],
[5,7, 8, 9, 15],
[12, 14, 16, 18],
[10, 11, 12, 13, 16, 17, 18, 20]
]

def explode_chains(encoded_lists):
    for sublist in encoded_lists:
            i=0
            while i<len(sublist)-2:
                if sublist[i]+1==sublist[i+1] and  sublist[i+1]+1==sublist[i+2]:
                    sublist.pop(i)
                    sublist.pop(i)
                    sublist.pop(i)
                else:
                    i+=1    

explode_chains(encoded_lists)
print(encoded_lists)
