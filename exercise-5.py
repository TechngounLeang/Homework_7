def backword_string_by_word(Sentence):
 
    
    return ' '.join(word[::-1] for word in Sentence.split(" "))
 
Sentence = input("Enter a string: ")
print(backword_string_by_word(Sentence))  
