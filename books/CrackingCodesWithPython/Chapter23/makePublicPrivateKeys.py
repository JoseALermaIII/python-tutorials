"""Public Key Generator

Implements series of functions capable of creating a `textbook RSA`_ public/private keypair and saves them to text
files.

Note:
    * https://www.nostarch.com/crackingcodes/ (BSD Licensed)
    * 'Textbook/Plain' RSA keys are not secure and should not be used to encrypt sensitive data.

.. _textbook RSA:
    https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA
"""

import random, sys, os
from books.CrackingCodesWithPython.Chapter13.cryptomath import gcd, findModInverse
from books.CrackingCodesWithPython.Chapter22.primeNum import generateLargePrime


def main():
    # Create a public/private keypair with 1024-bit keys:
    print('Making key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files made.')


def generateKey(keySize: int) -> tuple:
    """Generate public/private keypair

    Creates public/private keys keySize bits in size.

    Args:
         keySize: Bit size to make public/private keys.

    Returns:
        Tuples containing the public and private keypair split into their two halves.
    """
    p = 0
    q = 0
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q:
    print('Generating p prime...')
    while p == q:
        p = generateLargePrime(keySize)
        q = generateLargePrime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2 ** (keySize - 1), 2 ** keySize)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e:
    print('Calculating d that is mod inverse of e...')
    d = findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return publicKey, privateKey


def makeKeyFiles(name: str, keySize: int) -> None:
    """Make key files

    Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
    is the value in name) with the n,e and d,e integers written in
    them, delimited by a comma.

    Args:
         name: Name to append to public/private key files.
         keySize: Bit size to make public/private keys.

    Returns:
        None. Key files are created in current working directory.

    Note:
        * Checks if key files with given name already exist and exits with warning if so.

    """
    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % name) or os.path.exists('%s_privkey.txt' % name):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists!'
                 'Use a different name or delete these files and rerun this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % name)
    fo = open('%s_pubkey.txt' % name, 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % name)
    fo = open('%s_privkey.txt' % name, 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()


# If makePublicPrivateKeys.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()
