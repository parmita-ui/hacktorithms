# -*- coding: utf-8 -*-
"""ccg_game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AYfN_VtkKizVmK__5o2dgDDpRf3djasQ
"""

import random

print("Rules of the game are given below "+"\nEnter a number from 1 to 5 & match computer choice to ")
comp_score = 0
play_score = 0
while True:
      print("Violet=1 \nOrange=2 \nGreen=3 \nBlue=4 \nBlack=5 \n take a turn: " )
  #user input
  
      play_choice = int(input("User turn: "))

      while play_choice > 5 and play_choice < 1:
         play_choice=int(input("Enter a valid choice: "))
      if play_choice == 1:
        user_choice_color = 'Violet'
      elif  play_choice == 2:
        user_choice_color = 'Orange'
      elif play_choice == 3:
        user_choice_color = 'Green'
      elif play_choice == 4:
        user_choice_color = 'Blue'
      else:
        user_choice_color = 'Black'
       

      #printing user choice
      print("user color choice: " +user_choice_color)
      print("\n now computer's turn to choose")
      comp_choice = random.randint(1,5)
      while comp_choice == play_choice:
          comp_choice = random.randint(1,5)

      if comp_choice == 1:
        comp_choice_color = 'Violet'
      elif  comp_choice == 2:
        comp_choice_color = 'Orange'
      elif comp_choice == 3:
        comp_choice_color = 'Green'
      elif comp_choice == 4:
        comp_choice_color = 'Blue'
      else:
        comp_choice_color = 'Black'

      print("Computer color choice is: "+ comp_choice_color)

    #winning condition
      if(user_choice_color == comp_choice_color):
        play_score += 1
        print("Score of Player: " + str(play_score))
        print("Score of Computer: " + str(comp_score))
      else:
        comp_score += 1
        print("Score of Player: "+ str(play_score))
        print("Score of Computer: " + str(comp_score))
      print("Wanna play again? (Y/N)")
      ans = input()
      if ans == 'n' or ans == 'N':
        break

"""#Overall Result"""

if comp_score == play_score:
    print("Game Tied")
     
elif comp_score < play_score:
    print("Player is Victorious")
    print("<== User wins ==>")
    
elif comp_score > play_score:
    print("\n<== Computer wins ==>")
    print("\nPlayer is Defeated")