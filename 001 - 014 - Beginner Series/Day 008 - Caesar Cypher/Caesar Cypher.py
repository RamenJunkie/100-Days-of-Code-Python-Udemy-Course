import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  cypher = ""
  for i in text:
    if(i in alphabet):
        pos = alphabet.index(i)+shift
        while(pos > 25):
            pos -= 25
        cypher += alphabet[pos]
    else:
        cypher += i
    
  return cypher


def decrypt(text,shift):
    cypher = ""
    for i in text:
        if(i in alphabet):
            pos = alphabet.index(i)-shift
            while(pos < 0):
                pos += 25
            cypher += alphabet[pos]
        else:
            cypher += i
    
    return cypher

if(direction == "encode"):
    encrypted = encrypt(text,shift)
    print("Your encrypted message is: "+encrypted)
elif(direction == "decode"):
    decrypted = decrypt(text,shift)
    print("Your decrypted message is: "+decrypted)
else:
    print("Nothing to do.")
