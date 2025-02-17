myself = {
    "name":"floris",
    "age":13,
    "city":"The Hague"
}
print(myself)
print(myself["age"])
print(myself["city"])

list = ["floris",13 ,"The Hague"]
print(list[0])

print(myself.keys())

print(myself.values())

for i in myself.keys():
    print (i,myself[i])

if "hobby" in myself:
    print(myself["hobby"])
else:
    print("key doesn't exist")

myself["hobby"]="rugby"
print(myself)

del(myself["city"])
print(myself)

myself["age"]=14
print(myself)

myself["marks"]=[99,98,95,90]
print(myself)
print(myself["marks"][1])

c=len(myself)
print(c)