"""
FileName: ./pyfiles/Person.py

Py file for Person Class

    Class description:
    Super class for PenPal and Postie classes, acts as a general class for
    the two classes.

    Revisions:

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""


class Person:
    def __init__(self, name: str):
        self.name = name
        self.letter = None

    def __str__(self):
        return self.name

    def deliver_letter(self, receiver):
        receiver.letter = self.letter
        self.letter = None
        return
