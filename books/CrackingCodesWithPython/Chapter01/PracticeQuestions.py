# Chapter 1 Practice Questions
# SPOILERS: Chapter 5 (caesar cipher), 6 (caesar hacker), 7 (functions)
# Corrections submitted for Question 1, 3, 4, and 5


# caesarCipher from Chapter 5
def caesarCipher(key, message, mode):

    # Every possible symbol that can be encrypted (if encrypting by hand):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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


# caesarHacker from Chapter 6
def caesarHacker(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared:
        translated = ''

        # The rest of the program is almost the same as the Caesar program:

        # Loop through each symbol in message:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wraparound:
                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                # Append the decrypted symbol:
                translated += SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated += symbol

        # Display every possible decryption:
        print('Key #%s: %s' % (key, translated))
    return None


# 1. Encrypt the following entries from Ambrose Bierce's The Devil's Dictionary
#    with the given keys:
messages = ["AMBIDEXTROUS: ABLE TO PICK WITH EQUAL SKILL A RIGHT-HAND POCKET OR A LEFT.",
            "GUILLOTINE: A MACHINE WHICH MAKES A FRENCHMAN SHRUG HIS SHOULDERS WITH GOOD REASON.",
            "IMPIETY: YOUR IRREVERENCE TOWARD MY DEITY."]
keys = [4, 17, 21]

for index in range(len(keys)):
    print(caesarCipher(keys[index], messages[index], "encrypt"))

# 2. Decrypt the following ciphertexts with the given keys:
messages = ["ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTC XC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS.",
            "MQTSWXSV: E VMZEP EWTMVERX XS TYFPMG LSRSVW."]
keys = [15, 4]

for index in range(len(keys)):
    print(caesarCipher(keys[index], messages[index], "decrypt"))

# 3. Encrypt the following sentence with the key 0:
message = "THIS IS A SILLY EXAMPLE."
print(caesarCipher(0, message, "encrypt"))

# 4. Here are some words and their encryptions. Which key was used for each word?
print("\nHacking 'LIMYVOX':")
caesarHacker("LIMYVOX")
print("\nHacking 'PRDRDFKF':")
caesarHacker("PRDRDFKF")
print("\nHacking 'HZAYVUVTF':")
caesarHacker("HZAYVUVTF")

# 5. What does this sentence encrypted with key 8 decrypt to with key 9?
print("\nHacking 'UMMSVMAA: CVKWUUWV XIBQMVKM QV XTIVVQVO I ZMDMVOM BPIB QA EWZBP EPQTM.':")
caesarHacker("UMMSVMAA: CVKWUUWV XIBQMVKM QV XTIVVQVO I ZMDMVOM BPIB QA EWZBP EPQTM.")
