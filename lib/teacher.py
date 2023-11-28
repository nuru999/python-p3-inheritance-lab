#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self,first_name, last_name,knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "Programming is a valuable skill",
            "Python function definition",
            "Object-oriented programming concepts",
            "Python libraries and frameworks",
            "Web development with JavaScript",
            "Database design and management",
            "Software testing and debugging",
        ] 
   
    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)
        else:
            return None