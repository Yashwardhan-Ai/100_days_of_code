logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo,"\n Hello and Welcome to Richie Rich Auction!")

bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record) :
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record :
        bid_amount = bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner of the aution is {bidder} with the highest bid of {highest_bid}$!")


while not bidding_finished:
    name = input("PLease enter your name to register for the auction : ")
    price = int(input("Please enter your bid amount : Rs."))

    bid[name] = price
    procceed_or_stop = input("Is ther anyone who wants to chalenge this decision ! Please type 'Yes' or 'No' :").lower()
    if procceed_or_stop == "no":
        bidding_finished == True
        find_highest_bidder(bid)
        break





