"""
FileName ./encryptor.py

    Class Description:
    Encryptor class will contain two static methods:
    - encrypt
    - decrypt
    Encryptor class will be used by PenPal class (Alice and Bob)

By: Yoseph Campbell
Student ID: 20085059
Date Created: 20/10/2022
"""
class Encryptor:

    @staticmethod
    def encrypt(message: str):
        encrypted_message = ""
        for i in message:
            value = ord(i)
            value -= 1
            value = chr(value)
            encrypted_message += value
        return encrypted_message

    @staticmethod
    def decrypt(message: str):
        decrypted_message = ""
        for i in message:
            value = ord(i)
            value += 1
            value = chr(value)
            decrypted_message += value
        return decrypted_message

