alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def shif(sh):
    new_alphabet = alphabet[:]
    
    for i in range(sh):
        new_alphabet.append(new_alphabet.pop(0))
    # print(new_alphabet)
    return new_alphabet

def encrypt(text, shift):
    alphabet_c = shif(shift)
   
    new = ''
    for letter in text:
        if letter in alphabet:
            new += alphabet_c[alphabet.index(letter)]
        else:
            new += letter

    print(new)

def decrypt(text, shift):
    alphabet_c = shif(shift)

    new = ''
    for letter in text:
        if letter in alphabet:
            new += alphabet[alphabet_c.index(letter)]
        else:
            new += letter
    print(new)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def caesar():
    from art import logo
    print(logo)
    while True:        
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        word = input("Type your message:\n").lower()
        shift_n = int(input("Type the shift number:\n"))

        if direction == 'encode':
            encrypt(word, shift_n)
        else:
            decrypt(word, shift_n)
        
        guess = input("Do you wanna play again? [y] [n]").lower()
        if guess == 'n':
            break

caesar()
print("Thanks for play this game!")