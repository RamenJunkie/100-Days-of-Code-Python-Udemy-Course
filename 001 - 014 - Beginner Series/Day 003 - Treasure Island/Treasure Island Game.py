print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = True

while(direction == True):
  direction = input("Which direction would you like to go, left or right?\n")
  direction = direction.lower()

  #print(f"DEBUG: {direction}")
  
  if(direction == "l" or direction == "left"):
    direction = "left"
  elif(direction == "r" or direction == "right"):
    direction = "right"
  else:
    print("Please enter a valid direction.")
    direction = True


if(direction == "right"):
  print("You fall into a hole and are eaten by a Gnu!")
  exit()

print("You have reached a small lake, there is steam rising from the lake,\nyou are not sure if it's due to the temperature of the air or the water.")

while(direction == "left"):
  direction = input("Would you like to swim or wait for a boat?\n")
  direction = direction.lower()

  #print(f"DEBUG: {direction}")
  
  if(direction == "s" or direction == "swim"):
    direction = "swim"
  elif(direction == "w" or direction == "wait"):
    direction = "wait"
  else:
    print("Please enter a valid action.")
    direction = "left"

if(direction == "swim"):
  print("You plunge into the water.  It seems the steam was meerly due to the\nchilly air. You start to swim across the pond but suddenly feel something\nwrap itself around your ankle.  You think it might be some sort of tentacle\nbut you will never know as it quickly pulls you under and drowns you.")
  exit()

print("You wait a short while near the lake, unsure of how safe it is to swim across.\nAfter a short time, you notice the air becomes slowly more foggey, you\ncan hardly see across the lake now.  Suddenly there is a shadow in the fog approaching.\nA boat emergest from the fog.  It appears to be unpiloted but you swear you briefly glimpsed a ghastly spectre pushing it along for a brief moment.  It stops next to the shore waiting, and after a pause, you tentatively, you board the boat.\n\nIt immidiately starts to glide across the water, the foggy air making it hard to be sure where you are going.  After a brief period, you make out the other side of the shore approaching.  The boat gently flows to the edge and awaits for you to exit.  It then continues it's journey taking the fog along with it.\n\nWhen you turn to survey the island you see three trees, each with a door of a different color embedded in it.")

while(direction == "wait"):
  direction = input("Which door will you open?\n")
  direction = direction.lower()

  #print(f"DEBUG: {direction}")
  
  if(direction == "r" or direction == "red"):
    print("You open the red door.  The tree's leaves start to rustle faster and faster, and a howling wind begins to grow.  You start to feel pulled towards the now open door.  You attmpt to close the door to no avail, the tree now shaking violently and the howling has grown to be quite defening.  You are sucked inside and the door slams shut.  The ruckus calms down.\n\nYou see only darkness briefly before your view starts to become more clear.  You are now looking down at the clearing on the edge of the pond, where the three doors are.  You try to move but cannot, for you are now part of the curesed tree, forever.")
  elif(direction == "b" or direction == "blue"):
    print("You choose the blue door.  You reach for the handle but it seems to be stuck.  Giving it another twist, you manage to get the knob to turn slightly, as you do so, you notice the world around you become slightly dimmer.  You continue to turn the knob despite this and it becomes as dark as night the more you tun the knob.  Once it is pitch black, you feel the door pull slightly loose, a sliver of light showing from the edge of the doorway.\n\nYou open the door, and as you do the area is filled witht he light from inside the tree.  However the light reveals that you are no longer alone in the clearing, but are in fact now surrounded by several creatures of unimaginable horror and darkness.  They leer at you menacingly before leaping on you.\n\nThe door slowly shuts itself and as the knob returns to it's normal position, the daylight returns as normal, nothing but the empty clearing remains.")
  elif(direction == "y" or direction == "yellow"):
    print("You choose the yellow door.  You open the door and reveal a room that seems much too large to be inside this tree, which is quite large itself.  The room is filled with mountains of golden coins and glistening jewels.  You have found the treasure you have been seeking.  You enter the chamber, admiring the riches you now posess.\n\nThere is a slow creak and the door closes itself behind you.  You see part of a skeleton hanging from the door, it is as if the owner of the skeleton had been trying to claw throught he door and died int he process.  You return to the door and grip the handle to open it.  It stands fast.\n\nYou have found the treasure, but it seems you may never leave with it, or at all.\n\n   You win....?")
  else:
    print("You don't see that here.")
    direction = "wait"






print("The End")
  