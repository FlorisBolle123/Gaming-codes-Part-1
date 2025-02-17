textbooks = {  
    'math': 150,  
    'physics': 250,    
    'chemistry': 300  
}  

textbooks['physics'] = 200  

textbooks['biology'] = 220  
textbooks['english'] = 180  

book_name = input("Enter a book name: ")  

if book_name in textbooks:  
    print("The cost of", book_name, "is:", textbooks[book_name])  
else:  
    print("Book not found.")

for i in textbooks.keys():
    print(i,textbooks[i])