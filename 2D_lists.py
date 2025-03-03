dl=[[1,2,3], [4,5,6], [7,8,9]]
print(dl)

row=len(dl)
print(row)

columns=len(dl[0])
print(columns)

#print a real 2d list
for i in range(0,row):
    for j in range(0,columns):
        print(dl[i][j],end=' ')
    print("")

#take input from the user and ask for the number of rows and columns
rows=int(input("Enter the number of rows "))
cl=int(input("Enter the number of columns "))

nl = []

for i in range(rows):
    temp=[]
    for j in range(cl):
        x=int(input("Enter the element : "))
        temp.append(x)
    nl.append(temp)

for i in range(0,rows):
    for j in range(0,cl):
        print(nl[i][j],end=" ")
    print("\n")