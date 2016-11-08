from sys import exit

def countryside_forest():
    print "If you decide to go South you have to figure out where to get some food."
    print "There are plenty of berries and mushrooms in a forest."
    print "Do you decide to go there to pick some or do you decide to move along?"


    countryside_choice = raw_input ("> ")
    if "berries" in countryside_choice or "mushrooms" in countryside_choice or "forest" in countryside_choice:
        dead("In case you decide to eat some mushrooms or berries you are doomed. You are no expert and die of an intoxication.")

    elif "move" in countryside_choice or "along" in countryside_choice:
        print "You are lucky and still alive."
        countryside_man()
    else:
       dead("You are too slow.")

def countryside_man():

   print "While you cut across the fields you meet a kindly old man who offers you an apple."
   print "Do you decide to take the apple or to decline with thanks?"

   countryside_choice = raw_input ("> ")

   if "man" in countryside_choice or "apple" in countryside_choice:
     dead("In case you decide to take the apple you don't live much longer. The nice old guy turns into a very bad one, pulles out a knife and cuts off both your arms and feet.")

   if "decline" in countryside_choice or "thanks" in countryside_choice:
     print "In case you decide to decline with thanks you are still alive and also still hungry."
   else:
       dead("Wrong choice.")

def urban_territory_supermarket():
   print "If you decide to go West you have to figure out where to get some food."
   print "There is a huge supermarket, but crowded with Zombies."
   print "Do you decide to go in there and fight or run away?"

   urban_territory_choice = raw_input ("> ")
   if "supermarket" in urban_territory_choice or "fight" in urban_territory_choice:
       dead("In case you decide to fight them, you are realizing that that was not a bright idea. You don't have any martial art skills. Game over!")

   elif "run" in urban_territory_choice or "away" in urban_territory_choice:
       print "You are lucky and still alive."
       urban_territory_horse()
   else:
       dead("You are too slow, game over.")

def urban_territory_horse():

   print "While you are walking through the streets you detect a lonely horse in front of a barbers shop."
   print "Do you decide to hunt it down and eat it or move along?"

   urban_territory = raw_input ("> ")

   if "horse" in urban_territory or "hunt" in urban_territory:
     print "In case you decide to hunt and eat it: congratulations! Not only you satisfy your hunger, you also ate also the Anti-Zomie-Gen of the horse. You are unvourndable and able to rescue the world now!"

   elif "move" in urban_territory or "along" in urban_territory:
       dead("You will die hungry.")

   else:
       dead("You are too slow.")

def dead(why):
  print why, "Too bad."
  exit(0)

def start():
  print "Welcome to the zombie apocalypse 2018"
  print "You have to decide if you are heading West to urban territory or South into the countryside."
  print "Which one do you take?"

  choice = raw_input("> ")

  if "est" in choice:
    urban_territory_supermarket()
  elif "outh" in choice:
    countryside_forest()
  else:
    dead("You are eaten by Zombies.")


start ()
