
import random

lst = ['0001', '0011', '0101', '1011', '1101', '1111']

new_lst=[]
for binary_number in lst:
    decimal_number=int(binary_number,2)
    new_lst.append(decimal_number)

print(new_lst)

def crazy():
    r1=random.choice(new_lst)
    r2=random.choice(new_lst)
    r3=r1+r2
    new_lst.append(r3)
    new_lst.remove(r1)
    new_lst.remove(r2)


while len(new_lst)>2:
    crazy()
    print(new_lst)

print(f"Final iteration is {new_lst}")    
