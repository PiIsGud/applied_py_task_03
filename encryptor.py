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

if __name__ == "__main__":
    origin_message = "hi"
    encrypted_msg = Encryptor.encrypt(origin_message)
    decrypted_msg = Encryptor.decrypt(encrypted_msg)

    if decrypted_msg == origin_message:
        print("it works")
    else:
        print(f"it failed\noriginal: {origin_message}\nresult: {decrypted_msg}")