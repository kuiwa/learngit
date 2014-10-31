# -*- coding: utf-8 -*-

from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "Scene.enter()"
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		# be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"This is quips list",
	]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

    def enter(self):
        print "CentralCorridor.enter()"

        action = raw_input("> ")

        if action == "shoot!":
            print "action = shoot!"

        elif action == "dodge!":
            print "action = dodge!"

        elif action == "tell a joke":
            print "action = tell a joke"

        else:
            print "CentralCorridor.enter(), else"
            return 'central_corridor'
			
class LaserWeaponArmory(Scene):

    def enter(self):
        print "LaserWeaponArmory.enter() get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "guess right!"
            return 'the_bridge'
        else:
            print "guess wrong!"
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "TheBridge.enter(0"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print "EscapePod.enter()"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
         

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "Finished.enter()"
        return 'finished'
		
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
		
	def enter(self):
		print "Map.enter()"
		return 'MapEnter'
		
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()