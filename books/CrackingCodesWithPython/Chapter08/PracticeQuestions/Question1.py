# Using paper and pencil (*cough*), decrypt the following messages with the key 9.

from books.CrackingCodesWithPython.Chapter08.transpositionDecrypt import decryptMessage


def main():
    messages = ["H cb  irhdeuousBdi   prrtyevdgp nir  eerit eatoreechadihf paken ge b te dih aoa.da tts tn",
                "A b  drottthawa nwar eci t nlel ktShw leec,hheat .na  e soogmah a  ateniAcgakh dmnor  ",
                "Bmmsrl dpnaua!toeboo'ktn uknrwos. yaregonr w nd,tu  oiady hgtRwt   A hhanhhasthtev  e t e  eo"]

    key = 9

    for line in messages:
        print("%s| Len: %s" % (decryptMessage(key, line), len(line)))


# If Question1.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
