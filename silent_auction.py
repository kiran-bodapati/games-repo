import os
def find_winner(bidder_data):
 highest_bid=0
 winner=""
 for bidder in bidder_data:
     bidding_price=bidder_data[bidder]
     if bidding_price>highest_bid:
         highest_bid=bidding_price
         winner=bidder
 print(f"Here is the list of all the bidders {bidder_data}")
 print(f"The highest bidder is {winner} with bidding_price of {highest_bid}")
 




bidder_data={}
end_of_bidding=False
while  not end_of_bidding:
  
  name=input("what is your name?:")
  price=int(input("enter your bidding price:"))
  bidder_data[name]=price
  more_bidders=input("are there any bidders(yes/no)?").lower()
  if more_bidders=='no':
    end_of_bidding=True
    find_winner(bidder_data)
  elif more_bidders=='yes':
      os.system('clr')
