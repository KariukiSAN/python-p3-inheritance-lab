#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        if self.knowledge:
            index = random.randint(0, len(self.knowledge) - 1)
            return self.knowledge[index]
        else:
            return "I have no knowledge to share."