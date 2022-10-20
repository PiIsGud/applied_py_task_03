"""
FileName: ./letterbox.py

    Class Description:
    Letterbox class mimic the letterbox of the owner, each owner has their own letterbox
    Letterbox class has a state variable called flag_raised which is a boolean value
        - Letterbox flag will be raised if there is a letter in it (True)
        - Letterbox flag is lowered if there is no letters in it (False)

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""
class LetterBox:
    def __init__(self, owner):
        self.letter = None
        self.owner = owner
        self.flag_raised = False

    def raise_flag(self):
        self.flag_raised = True


