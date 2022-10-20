"""
FileName: ./postie.py

    Class Description:

    Functional Requirements:

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
        super().deliver_letter(receiver)
        