import colorama
from colorama import Fore, Back, Style
import requests
import random
import string

print(Fore.MAGENTA + """
      ╦  ╦┌─┐┌─┐┌─┐┬ ┬ ┬─┐
      ╚╗╔╝├─┤├─┘│ ││ │ ├┬┘
       ╚╝ ┴ ┴┴  └─┘└─┘ ┴└─""")
print(Fore.BLUE + """[ VAPOUR TOOL | V1 | NAIL TOOLS ]""")

print(Fore.CYAN + """
1. REPLIT
2. GITHUB
3. TWITTER
4. DISCORD VANITY
5. INSTAGRAM
6. EPIC GAMES
7. YOUTUBE HANDLE
8. SOUNDCLOUD
9. FACEBOOK
10. TWITCH
11. CREDITS
12. EXIT
""")
choice = int(input("\nPlease choose a serice: "))

if choice == 1:
  print(Fore.CYAN + "\n\n4L REPLIT NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of replit names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://replit.com/@' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")



if choice == 2:
  print(Fore.CYAN + "\n\n4L GITHUB NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of GITHUB names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://github.com/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")


  
if choice == 3:
  print(Fore.CYAN + "\n\n4L TWITTER NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of GITHUB names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://twitter.com/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")


if choice == 4:
  print(Fore.CYAN + "\n\n4L DISCORD VANITY GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of GITHUB names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://discord.com/api/v9/invites/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")
  
if choice == 5:
  print(Fore.CYAN + "\n\n4L INSTAGRAM NAME GEN/CHECKER (gets rate-limmed quickest)")
  amount = int(input("\nPlease enter the amount of INSTAGRAM names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://instagram.com/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")

if  choice == 6:
  print(Fore.CYAN + "\n\n4L EPIC GAMES NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of EPIC GAMES names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://fortnitetracker.com/profile/all/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")

if  choice == 7:
  print(Fore.CYAN + "\n\n4L YOUTUBE HANDLE GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of YOUTUBE handles you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://youtube.com/@' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")

if  choice == 8:
  print(Fore.CYAN + "\n\n4L SOUNDCLOUD NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of SOUNDCLOUD names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://soundcloud.com/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")

if  choice == 9:
  print(Fore.CYAN + "\n\n4L FACEBOOK NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of FACEBOOK names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://facebook.com/' + user)

if choice == 10:
  print(Fore.CYAN + "\n\n4L TWITTER NAME GEN/CHECKER")
  amount = int(input("\nPlease enter the amount of TWITTER names you want to check: "))
  for i in range(0, amount):
    user = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    r = requests.get('https://twitch.com/' + user)
    if r.status_code == 200:
      print(Fore.RED + user + " is taken")
    else:
      print(Fore.GREEN + user + " is avalible")

if choice == 11:
  print(Fore.MAGENTA + "\n\nVAPOUR NAME GEN/CHECKER CREDITS")
  print(Fore.CYAN + "MADE BY NAILDEV")

if choice == 12:
  exit()











  
