userReply = input("Would you like to buy stamps buy an envelope, or make a copy? ")
userl=userReply.lower()
if userl == "stamps":
    print("We can help you ship that package!")
elif userl == "envelope":
    print("We have many envelope sizes to choose from.")
elif userl == "copy":
    copies = input ("How many copies would you like? (Enter a number)")
    print("Here are {} copies." .format(copies))
else:
    print ("Thank you, please come again.")
