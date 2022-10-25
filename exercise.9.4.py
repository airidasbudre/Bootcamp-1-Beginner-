import os

bid_log = []
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_bid(new_name, new_bid):
    add_country = {}
    add_country["name"] = new_name
    add_country["bid"] = new_bid
    bid_log.append(add_country)


#🚨 Do not change the code below
print(bid_log)
bid_finished = False

while not bid_finished:
   a = input("Input your name: ")
   b = input("Input your Bid: $ ")
   add_new_bid(a, b)
   decision = input("If you wanna add another bid write 'Yes' if not write 'No': ")
   if decision == "Yes" or decision == "yes":
      bid_finished = False
      os.system('cls')
   elif decision == "No" or decision == "no": 
      bid_finished = True
      highest_bid = 0
      for i in bid_log:
         if highest_bid == 0:
            highest_bid = i["bid"] 
            Bidder_name = i["name"]
         else:
            if  highest_bid < i["bid"]:
               highest_bid = i["bid"] 
               Bidder_name = i["name"]
      print("The winner is " + Bidder_name + highest_bid)


  