
#using details as an example
details = ("Floris", 13, "green", "netherlands")

address = ("18", "The Hague", "south-holland","2596BT")

for x in address:
    print(x, end=' ')

houseno, city, area, postcode = address

#using print function with the tuple
print()
print("hno. ", houseno)
print("city. ", city)
print("area. ", area)
print("postcode. ", postcode)

#using integers in a tuple
my_tuple=3,5.2,"Golden retriever"
print(my_tuple)

#list inside a tuple
nested=(["apple","banana","orange"], "colors", ("red","yellow","pink"))

print (nested[1][1])
print(nested[0][1])
print(nested[2][1])

name = ("f","l","o","r","i","s","b","o","l","l","e")

print(name[1:4])
print(name[:-9])
print(name[9:])
print(name[:])

nested[0][1]="kiwi"
print(nested[0][1])

#creating a tuple known as programiz
prog = ("P","r","o","g","r","a","m","i","z")

print(prog[0:3])
print(prog[7:])
print(prog[0:2])

