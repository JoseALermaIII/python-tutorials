"""Chapter 6 Practice Questions

Answers Chapter 6 Practice Questions via Python code.

Break the following ciphertext one line at a time because each line has a different key.
Remember to escape any quote characters

Note:
    Contains spoilers for chapter 7 (functions)
"""

from books.CrackingCodesWithPython.Chapter01.caesarHacker import hackCaesar


def main():
    ciphertext = ["qeFIP?eGSeECNNS,",
                  "5coOMXXcoPSZIWoQI,",
                  "avnl1olyD4l'ylDohww6DhzDjhuDil,",
                  "z.GM?.cEQc. 70c.7KcKMKHA9AGFK,",
                  "?MFYp2pPJJUpZSIJWpRdpMFY,",
                  "ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K",
                  "Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA"]  # ROFL

    for line in ciphertext:
        print(hackCaesar(line))
        input("Press enter to continue\n")


# If PracticeQuestion.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
