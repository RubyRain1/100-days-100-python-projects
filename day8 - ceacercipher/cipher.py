
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cont = True
while cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #decryption and encryption files
    def encrypt(text, shift):
        messagel = [*text]
        encodeL = []
        finalL = []
        for i in range(0,len(text)):
            x = alphabet.index(messagel[i])
            x2 = x + shift
            encodeL.append(x2)
            finalL.append(alphabet[encodeL[i]])
        result = ''.join(finalL)
        print(f"Here is the encoded result: {result}")

    def decrypt(text, shift):
        messagel = [*text]
        encodeL = []
        finalL = []
        for i in range(0,len(text)):
            x = alphabet.index(messagel[i])
            x2 = x - shift
            encodeL.append(x2)
            finalL.append(alphabet[encodeL[i]])
        result = ''.join(finalL)
        print(f"Here is the decoded result: {result}")

    
    #program logic

    if direction == "encode":
        encrypt(text,shift)
                
    elif direction == "decode":
        decrypt(text,shift)
    userI = input("would you like to continue: ('yes' or 'no') ").lower()   
    if userI == 'yes':
        cont = True
    elif userI == 'no':
        cont = False