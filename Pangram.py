#Result: counting the number of vowels in a sentence
sentenece = input("Enter a String please: ")
Vowels ={
    "i":0,
    "e":0,
    "a":0,
    "u":0,
    "o":0
}
for letter in sentenece:
    if letter in Vowels:
        Vowels[letter] +=1
print(Vowels)

number = input("Enter a number: ")
numcount = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}

for n in number:
    if n in numcount:
        numcount[n]+=1

pangram = True
for count in numcount.values():
    if count==0:
        pangram = False

if pangram == True:
    print("this is a pangram number")
else:
    print("This is not a pangram number")