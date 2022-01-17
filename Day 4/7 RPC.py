rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
dict_game = {"r": rock, "p": paper, "s": scissors}

choice = input("Rock, paper or scissor?").lower()[0]
ai = random.choice(['r', 'p', 's'])
print(f"Player : {dict_game[choice]}\nAI:{dict_game[ai]}\n Player {'win!' if ( (choice == 'r' and ai == 's') or (choice =='s' and ai =='p') or (choice =='p' and ai =='r' )) else 'lose...' if ((choice == 'r' and ai == 'p') or (choice == 'p' and ai == 's') or (choice == 's' and ai =='r')) else 'draw.'}")