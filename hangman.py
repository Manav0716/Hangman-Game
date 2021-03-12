import random
from handman words import word_list
from handman logo import logo
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
#w1=input("enter a word")
l1=[]
for i in range(0,len(chosen_word)):
               l1+='_'
life=6
end_of_game = False
print("logo")
               
while (not end_of_game  ):        
    w1=input("enter a word")
    if w1 in l1:
        print("you have already guessed this word...try another word")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==w1:
            l1[position]=letter
    print(l1)
    if w1 not in chosen_word:
        print(stages[life])
        life-=1
        if life == -1:
            end_of_game= True
            print("Better luck next time")
    if "_" not in l1:
        end_of_game = True
        print("You win.")

    
#print(l1)

    
