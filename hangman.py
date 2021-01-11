import random
 
name = input("What is your name? ")
 
print("Welcome to Hangman ", name)

entered_letters =""

words = list()
text = open("words.txt", "r") 
for line in text: 
    
    line = line.strip()
    words.append(str.lower(line))

word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
tries = 6
 
 
while tries > 0:

    failed = 0
     
    for char in word: 
         
        if char in guesses: 
            print(char)
             
        else: 
            print("_")
           
            failed += 1
             
 
    if failed == 0:
        
        print("You Win") 
         
        print("The word is: ", word) 
        break
     
    guess = input("already entered letters:"+entered_letters+"\nguess a character: ")
    entered_letters+=guess
    
    guesses += guess 
     
    
    if guess not in word:
         
        tries -= 1
          
        print("Wrong")
         
        print("You have", + tries, 'more guesses')
         
         
        if tries == 0:
            print("You Loose the word was : ", word)
