import random  

marks = [random.randint(0, 100) for i in range(20)]  

ma30 = []  
ma31_69 = []  
ma70 = []  

for mark in marks:  
    if mark <= 30:  
        ma30.append(mark)  
    elif 31 <= mark <= 69:  
        ma31_69.append(mark)  
    else:  
        ma70.append(mark)  
 
print("Marks <= 30:", ma30)  
print("Marks between 31 and 69:", ma31_69)  
print("Marks >= 70:",  ma70)  