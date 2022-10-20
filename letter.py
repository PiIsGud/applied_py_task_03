"""
FileName: ./letter.py

Py file for Letter class

    class description:
    Letter class that contains details of the sender, receiver and a message

    Functional requirements:
    - Should be able to instantiate a Letter with a Sender, Receiver and default message

    Revisions:

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""


class Letter:
    def __init__(self, sender, receiver, message: str = "default"):
        self.sender = sender
        self.receiver = receiver
        self.is_read = False

        if message == "default":
            self.message = f"Hi {sender}, this is {receiver}"
            return
        else:
            self.message = message