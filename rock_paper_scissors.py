import random
rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
random_computer = random.randint(0,2)
User_choice = input("Please select from Rock, Paper , Scissors.").lower()
if random_computer == 0 and User_choice == "rock" :
    print(f"Computer chose {rock1}\n You chose {rock1}\n It's a tie!")
elif random_computer == 0 and User_choice == "paper" :
    print(f"Computer chose {rock1}\n You chose {paper1}\n You won!")
elif random_computer == 0 and User_choice == "scissors" :
    print(f"Computer chose {rock1}\n You chose {scissors1}\n Computer won!")
elif random_computer == 1 and User_choice == "rock" :
    print(f"Computer chose {paper1}\n You chose {rock1}\n Computer won!")
elif random_computer == 1 and User_choice == "paper" :
    print(f"Computer chose {paper1}\n You chose {paper1}\n It's a tie!")
elif random_computer == 1 and User_choice == "scissors" :
    print(f"Computer chose {paper1}\n You chose {scissors1}\n You won!")
elif random_computer == 2 and User_choice == "rock" :
    print(f"Computer chose {scissors1}\n You chose {rock1}\n You won!")
elif random_computer == 2 and User_choice == "paper" :
    print(f"Computer chose {scissors1}\n You chose {paper1}\n Computer won!")
elif random_computer == 2 and User_choice == "scissors" :
    print(f"Computer chose {scissors1}\n You chose {scissors1}\n It's a tie!")