import pyperclip
def main():
    myMessage = input('Enter your message:')
    myKey = 200
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)
def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key 
    return ''.join(ciphertext)
if __name__ == '__main__':
    main()  
