from art import logo ,vs
from data_sheet import data
import random
from replit import clear


def format_account(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, {account_description}, from {account_country}")

def check_answer(guess, guess_a_followers , guess_b_followers):

    if guess_a_followers > guess_b_followers :
        return guess == "a"
    else :
        return guess == "b"
    
score = 0

account_random_b = random.choice(data)

game_should_continue = True

while game_should_continue:
    print(logo)
    account_random_a =account_random_b
    account_random_b = random.choice(data)
    if account_random_a == account_random_b:
        account_random_b = random.choice(data)
    print(f"Compare 'A':{format_account(account_random_a)}")
    print(vs)
    print(f"Compare 'B':{format_account(account_random_b)}")

    guess = input("Who has more followers 'A' or 'B':").lower()

    guess_a_followers = account_random_a["follower_count"]
    guess_b_followers = account_random_b["follower_count"]

    is_correct = check_answer(guess, guess_a_followers, guess_b_followers)

    clear()
    
    if is_correct :
        score += 1
        print(f"You're right! Current Score = {score}")
    else:
        game_should_continue = False
        print(f"You got it wrong! Final score = {score}")
