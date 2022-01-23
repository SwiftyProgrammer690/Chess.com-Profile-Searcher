#Copyright @SwaritChoudhari [-:
#I you want to use this, please credit me!

#importing Stuff
from asyncio import gather
from chessdotcom.aio import get_player_profile, Client

#Defines how to get the user data from the chess.com API
def getMultipleUsernames(a, b, c, d):
  Client.aio = True
  usernames = [a, b, c, d]
  cors = [get_player_profile(name) for name in usernames]
  responses = Client.loop.run_until_complete(gather(*cors))
  print(responses)
def getOneUsername(a):
  usernames = [a]
  cors = [get_player_profile(name) for name in usernames]
  responses = Client.loop.run_until_complete(gather(*cors))
  print(responses)

#Main input for user
oneOrMultiple = input("Would you like to (1) search for multiple username or (2) search one username?\n")

#Tells what to do with the input
if oneOrMultiple == '1':
  print("Type in four usernames, one for each prompt please! Please make sure these are valid chess.com usernames!")
  userSearch1 = input("What username for this prompt 1?\n ")
  userSearch2 = input("What username for this prompt 2?\n ")
  userSearch3 = input("What username for this prompt 3?\n ")
  userSearch4 = input("What username for this prompt 4?\n ")
  getMultipleUsernames(userSearch1, userSearch2, userSearch3, userSearch4)
elif oneOrMultiple == '2':
  userName = input("Who would you like to search up? Make sure it is valid! ")
  getOneUsername(userName)
else:
  print("Please run the program again and give a valid input.")