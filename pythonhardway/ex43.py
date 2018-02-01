from sys import exit
import random

class Scene(object):

    def enter(self):
        print("You have just been attacked from nowhere.")
        exit(0)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        print("Gothons From Planet Percal #25 have invaded our space ship.")
        print("What will you do?")

        while True:
            next_scene = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene)

class Death(Scene):

    def enter(self):
        print("You're dead.")
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print("You stand at the central corridor.")
        return "death"

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You reached the Armory.")

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):
    scenes = {
        "central corridor": CentralCorridor(),
        "laser weapon armory": LaserWeaponArmory(),
        "the bridge": TheBridge(),
        "escape pod": EscapePod(),
        "death": Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()
