from art import logo
from os import system
print(logo)
print("Welcome to the Secret Auction")
bidding_results = {}
highest_bid = 0
winner = ""
while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidding_results[name] = bid
    ask = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if ask == "yes":
        print("\n"*100)
        continue
    elif ask == "no":
        break
for i in bidding_results:
    if bidding_results[i] > highest_bid:
        highest_bid = bidding_results[i]
        winner = i
print(f"The winner is {winner} with a bid of ${highest_bid}")