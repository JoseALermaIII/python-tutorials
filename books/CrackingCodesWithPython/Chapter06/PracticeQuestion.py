# Break the following ciphertext one line at a time because each line has a different key.
# Remember to escape any quote characters
# SPOILER for chapter 7 (functions)


def decryptCaesar(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

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

ciphertext = ["qeFIP?eGSeECNNS,",
              "5coOMXXcoPSZIWoQI,",
              "avnl1olyD4l'ylDohww6DhzDjhuDil,",
              "z.GM?.cEQc. 70c.7KcKMKHA9AGFK,",
              "?MFYp2pPJJUpZSIJWpRdpMFY,",
              "ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K",
              "Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA"]  # ROFL

for line in ciphertext:
    print(decryptCaesar(line))
    input("Press enter to continue\n")
