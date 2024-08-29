#The Caesar Cipher

# An encoder/decoder for our spies to secretly send messages.

encryption_option = input("Would you like to Encode or Decode? ")
cipher_num = int(input("What is your cipher number? "))
text = input("What is your message? ")

# should_encode will be true if the user 
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.

#A-Z = 65 to 90
#a-z = 97 to 122

new = ""


punc = [" ", ".", "!", "?", '"', "'", ":", ",", ";", "=", ">", "<", "_", "-", "/"]

if encryption_option != should_encode or encryption_option != should_decode:
    # Print a nice notice that we only support encrypt/decrypt
    # Your code here!
    print("We only support encrypt/decrypt")
    pass

elif should_encode:
    # Your code here!
    for char in text:
        if char in punc:
            new += char
        else:
            if "A" <= char <= "Z":
                new += chr((ord(char) + cipher_num - 65) % 26 + 65)
            elif "a" <= char <= "z":
                new += chr((ord(char) + cipher_num - 97) % 26 + 97)
        
    pass

elif should_decode:
    # Your code here!
    for char in text:
        if char == " ":
            new += " "
        else:
            if "A" <= char <= "Z":
                new += chr((ord(char) - cipher_num - 65) % 26 + 65)
            elif "a" <= char <= "z":
                new += chr((ord(char) - cipher_num - 97) % 26 + 97)
    pass



print(new)
