"""
FileName: ./postie.py

    Class Description:
        Postie Class inherits from Person class

    Functional Requirements:
        - Receives letter from the post office
        - delivers letter from post office to the recipient PenPal Letterbox

    Revision:

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""
from person import Person


class Postie(Person):
    def __init__(self, name):
        super().__init__(name)

    def receive_letter(self, post_office: "PostOffice"):
        self.letter = post_office.letter
        post_office.letter = None

    def deliver_letter(self, receiver: "PenPal"):
        super().deliver_letter(receiver.letter_box)
        