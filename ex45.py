from sys import exit

class Scene(object):
    def enter(self):
        pass

    def WrongDecision(self):
        print "If it takes you too long to decide you will suffocate and die."
        return 'dead'

class Hole(Scene):

     def enter(self):
         print "You are on your way home from work."
         print "It has been an exhausting day,"
         print "your college Jonathan was stressing you out"
         print "with work tasks you could barely handle."
         print "You are so absorbed by your thoughts that you miss a road sign."
         print "Now you are walking in the middle of a construction site."
         print "Before you know it your right foot slips"
         print "and you are falling into a deep dark whole."
         print "Slowly your eyes get used to the darkness"
         print "and you realize where you are."
         print "Luckily you are not insured at all, only a few scratches."
         print "You try to call someone for help, but nobody answers."
         print "You starting to prepare yourself for the night"
         print "when you suddenly detect something slightly shimmering on the other side of the whole."
         print "You have to find out what it is. A treasure? Or something that might help you get out of here?"
         print "Are you prepared to find out what it is?"

         action = raw_input("> ")

         if action == "Yes" or action == "yes":
             print "Getting closer you realize that the glowing is a reflection of a doorknob."
             print "It is still very dark but standing right in front of it"
             print "makes you realize that this must be an old ornamented antique door."
             print "You are asking yourself if you are dreaming."
             print "You cannot help yourself but entering the door."
             print "The sound of the opening noice tells you that the door has not been opened much"
             print "In the first place you can't see anything."
             print "But then you realize that you are standing in some sort of hallway with four other doors."
             print "Are you curious and just entering the first door?"
             return 'decision'
         elif action == "No" or action == "no":
             print "You move on to the other doors."
             print "Which one will you take?"
             return 'decision'
         else:
            print "You have to decide!"
            return 'hole'

class Decision(Scene):

    def enter(self):
        print "You have a hard time to decide which door to take next."
        print "Each of them look exactly the same."
        print "Will you be brave and choose one or go back to the hole?"

        decision = raw_input("> ")

        if "1" in decision or "first" in decision:
            print "When you enter the first door some sort of a hurricane takes you away."
            print "You traveled back in time and are watching yourself walking into that construction sight."
            print "This time you manage to not fall into that hole"
            print "but a crane drops a very big stone on your head. You're dead."
            return 'dead'
        elif "2" in decision or "second" in decision:
            print "When you enter the second door you are suddenly in a magical forest."
            print "A purple fat cat is sitting on a tree and talking to you."
            print "Obviously she has lost her marbles"
            print "but she claims to know a way out and you find yourself.."
            return 'hallway'
        if "3" in decision or "third" in decision:
            print "When you enter the third door you find yourself in a large room where everything is out of pure gold."
            print "You can't belief how rich you are all of a sudden"
            print "and you start to dream what you could buy from all that money."
            print "But while you were distracted an oversized paymachine is rolling towards you and about to crush you."
            return 'dead'
        elif "4" in decision or "fourth" in decision:
            print "Behind the fourth door you can find only spiral staircase high as a skyscraper."
            print "It does seem to end in a big fluffy cloud with a rainbow."
            print "You have to catch your breath after the first 200 stairs, because it is really high."
            print "But then you see something that looks like traffic lights, you are back on the crossroad"
            print "that you passed before you walked into the construction sight."
            return 'outside'
        else:
            self.WrongDecision()

class Hallway(Scene):

    def enter(self):
        print "You are back in the hallway."
        print "Do you want to go back to the hole and risk not getting found"
        print "Or try another door?"

        return 'finished'

class Outside(Scene):

    def enter(self):
        print "Somehow you really managed to get outside. Congratulations!"
        print "You are still alive"
        print "and able to finish the work your college Jonathan asked you to finish till tomorrow."

        return 'finished'

    lost = ['dead']

    def enter(self):
        print Death.lost
        exit(1)


class Map(object):

     scenes = {
     'hole' : Hole(),
     'decision' : Decision(),
     'hallway' : Hallway(),
     'outside': Outside(),
     }

     def __init__(self, start_scene):
         self.start_scene = start_scene

     def next_scene(self, scene_name):
         val = Map.scenes.get(scene_name)
         return val

     def opening_scene(self):
         return self.next_scene(self.start_scene)
