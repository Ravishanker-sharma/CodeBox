string = input(":")
print(string)
lis= list(map(str,string.split()))
lis2 = []
for i in lis :
    if i.isnumeric():
        lis2.append(i)
print(lis)
print(lis2)
