"""
FileName: ./pyfiles/PenPal.py

Py file for PenPal class

    Class description:
    Child class of the super class Person.

    Functional Requirements:
    - Will be able to create a letter
    - Deliver the letter to PostOffice
    - Ability to read the letter
    - Ability to encrypt and decrypt message in letters upon creation

    Revisions:

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""
from person import Person
from letterbox import LetterBox
from letter import Letter
from encryptor import Encryptor


class PenPal(Person):

    def __init__(self, name):
        super().__init__(name)
        self.letter_box: LetterBox = LetterBox(self)

    def create_letter(self, receiver, message="default"):
        self.letter = Letter(self, receiver, message)
        return

    def encrypt(self):
        if self.letter is None:
            return "cannot encrypt when I dont have a letter"
        else:
            self.letter.message = Encryptor.encrypt(self.letter.message)
            return "encrypted the letter"

    def decrypt(self):
        if self.letter is None:
            return "cannot decrypt when I dont have a letter"
        else:
            self.letter.message = Encryptor.decrypt(self.letter.message)
            return "decrypted the letter"

    def retrieve_letter(self):
        self.letter = self.letter_box.letter

    def read(self):
        if self.letter is not None:
            self.decrypt()
            return f"the letter reads: {self.letter.message}"


