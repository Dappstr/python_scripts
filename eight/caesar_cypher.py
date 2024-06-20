def encode(n):
    msg = input("Enter message to encode: ")
    encoded = []
    for i in range(0, len(msg)):
        encoded += chr(ord(msg[i]) + n)
    encoded_msg = ''.join(encoded)
    return encoded_msg


def decode(n):
    msg = input("Enter message to decode: ")
    decoded = []
    for i in range(0, len(msg)):
        decoded += chr(ord(msg[i]) - n)
    decoded_msg = ''.join(decoded)
    return decoded_msg

not_quit = True

while not_quit:
    print("Caesar Cypher encoder and decoder")
    choice = input("Type \'encode\' to encode, or \'decode\' to decrypt: ").lower()
    if choice == "encode":
        rot = int(input("Enter amount to rotate by: "))
        encoded_msg = str(encode(rot))
        print(f"Your encoded message is: {encoded_msg}")
    elif choice == "decode":
        rot = int(input("Enter amount to rotate by: "))
        decoded_msg = str(decode(rot))
        print(f"Your decoded message is: {decoded_msg}")
    elif choice == "quit" or choice == "Quit":
        not_quit = False