#!/usr/bin/env python

class human():
    '''This is a human class'''

    def __init__(self, human_gender = "unknown", age = 0, mungry_level="peaceful", hunger_level=0):

        self.human_gender = human_gender
        self.age = age
        self.mungry_level = mungry_level
        self.hunger_level = hunger_level

    def setGender(self):
        self.human_gender = input("Please enter human's gender:")

    def setAge(self):
        self.age = int(input("Please enter human's age"))

    def setHunger_level(self):
        self.hunger_level = int(input("Please enter human's hunger level (0-10)"))

    def changeMungry_level(self):
        if 0 <= self.hunger_level < 4:
            self.mungry_level = "Human is currently peaceful"
        elif 4 <= self.hunger_level < 8:
            self.mungry_level = "Human is now getting narky"
        elif 8 <= self.hunger_level <= 10:
            self.mungry_level = "HUman is now aggressive! Watch out!"
        return (self.mungry_level)

MrWickins = human()

MrWickins.setGender()
MrWickins.setAge()
MrWickins.setHunger_level()

print ("The human is a: ", MrWickins.human_gender)
print ("The human is: ", MrWickins.age)
print ("The humans hunger level is: ", MrWickins.hunger_level)
print (MrWickins.changeMungry_level())
