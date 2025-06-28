#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
                            "str is a data type in Python",
                            "programming is hard, but it's worth it",
                            "JavaScript async web request",
                            "Python function call definition",
                            "object-oriented teacher instance",
                            "programming computers hacking learning terminal",
                            "pipenv install pipenv shell",
                            "pytest -x flag to fail fast",
                        ]

    def teach(self):
        # Create a random index of the array passing the array length as the range
        random_index = random.randint(0,len(self.knowledge)-1)
        print(random_index)
        return self.knowledge[random_index]

test = Teacher("Eric", "Brian")
print(test.first_name)
print(test.last_name)
print(test.knowledge)
test.teach()