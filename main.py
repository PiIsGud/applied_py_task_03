"""
FileName: ./main.py

Py file for main

    file description:
    Integrates all the classes to ensure that they are running smoothly

    functional requirements:
    - The main python module should be able to send letters to bob and alice
    - the number of back and forth conversation between bob and alice can be changed by changing the number of turns

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""
from penpal import PenPal
from postie import Postie
from postoffice import PostOffice

def play(sender: PenPal, receiver:PenPal):
    postman = Postie("Charli")
    post_office = PostOffice()
    sender.create_letter(receiver)
    print(f"{sender} created a letter for {receiver}")
    sender.encrypt()
    print(f"{sender} has encrypted the letter!")
    sender.deliver_letter(post_office)
    print(f"{sender} has dropped letter to post office")
    postman.receive_letter(post_office)
    print(f"{postman} received letter from postoffice")
    postman.deliver_letter(receiver)
    print(f"{postman} delivered letter to {receiver} letterbox")
    receiver.letter_box.raise_flag()
    print(f"{receiver} letterbox is raised")
    receiver.retrieve_letter()
    print(f"{receiver} got letter from letterbox, flag is lowered")
    receiver.decrypt()
    print(f"{receiver} decrypted the letter")
    receiver.read()
    print(f"{receiver} read the letter")


if __name__ == '__main__':
    alice = PenPal("Alice")
    bob = PenPal("Bob")
    turn = [1,2,3,4]
    sender = alice
    receiver = bob
    for n_turns in turn:
        play(sender, receiver)
        if sender is alice:
            sender = bob
            receiver = alice
        else:
            sender = alice
            receiver = bob