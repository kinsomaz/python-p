import pyperclip, affineCipher, detectENGLISH, cryptomath
SILENT_MODE = False
def main():
    myMessage = """|*W#G!ZYFI W~GYm6W6I3I kIWFGWoIW#]mmI6W54FImm5nI4FW5\W5FW#GYm6W6I#I5kIW]W"Y!]4W54FGWoIm5Ik54nWF"]FW5FW~]3W"Y!]4A|W.*m]4WrY 54n"""
    hackedMessage = hackAffine(myMessage)
    
    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.') 

def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
        if detectENGLISH.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')

            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main() 
            
             









            
            
