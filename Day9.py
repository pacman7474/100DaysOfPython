import os

more_bidders = True
bidder_info = {}

while more_bidders:
    print("Welcome to the secret auction program")
    name = input("What is your name?: ")
    bid = int(input(f"Hello {name}, what is your bid?: $"))
    bidder_info[name] = bid
    cont_bidding = input("Are there more bidders (Y/N): ").upper()
    if cont_bidding == "N":
        more_bidders = False

    os.system('cls')
highest_bidder = max(bidder_info,key=bidder_info.get)

#for bid_name in bidder_info:
##    if bidder_info[bid_name] > highest_bid:
#        highest_bidder = bid_name
#        highest_bid = bidder_info[bid_name]
print(f"The highest bidder was {highest_bidder} with a bid of ${bidder_info[highest_bidder]}")