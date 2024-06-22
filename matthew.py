# One player is Matthew, rest are the band. The band knows the location, Matthew doesn't.
# Players ask each other questions to figure out who is Matthew. If Matthew is found in under 5 minutes, the others win; otherwise Matthew wins.
# Run script to assign roles, see your role in private, then hide it and pass device to next player.
import os, random, getpass
player_count = 5
locations = ["batı park", "-3 stüdyo", "sağlık merkezi", "bova",
             "kaş kamping", "LOOP", "henry çimenler", "ç1d1",
             "tuvalet", "ecenin evi", "sticky's", "anne rahmi", "matrix",
             "sedir42", "iskele balık", "l'apero", "zorlupsm sigara mekani"]
spy_i = random.randint(1, player_count)
location = random.choice(locations)
os.system('cls')
for i in range(1, player_count+1):
    getpass.getpass("enter to see")
    os.system('cls')
    print("matthew over here" if i == spy_i else f"great band at '{location}'")
    getpass.getpass("enter to hide")
    os.system('cls')