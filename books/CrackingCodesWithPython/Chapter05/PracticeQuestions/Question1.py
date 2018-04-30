# Using caesarCipher.py, encrypt the following sentences with the given keys
# SPOILER for Chapter 7 (functions)

def caesarCipher(key, message, mode):

    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Store the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    return translated


messages = ["'You can show black is white by argument,' said Filby, 'but you will never convince me.'",
            "1234567890"]
keys = [8, 21]

for index in range(len(keys)):
    print(caesarCipher(keys[index], messages[index], "encrypt"))
