**Note:** My PDF copy was created *12/1/2017 7:03:06PM* and was last modified  *12/4/2017 5:30:14PM*

* Chapter 1 Practice Questions:

~~The answer for Practice Question 1, part b: Encrypt “GUILLOTINE: A machine which makes a Frenchman shrug his shoulders with good reason.” with a key of 17 should be “XlZccfkZeV:NRN4rtyz5vN.yztyN4r2v0NrNW9v5ty4r5N0y9!xNyz0N0y6!3uv90N.z yNx66uN9vr065Q”, not “bpdggjodiZ:RVR8vx349zRD34x3R8v6z.RvRa?z9x38v9R.3?B2R34.R.30B7yz?.RD4A3R200yR?zv.09U” (that’s key of 21)~~

Scratch that, with SYMBOLS = “ABCDEFGHIJKLMNOPQRSTUVWXYZ”, even the messages should be in all caps with totally different outputs, like the decryption in question 2.

Question 1 answers should be:

a. EQFMHIBXVSYW: EFPI XS TMGO AMXL IUYEP WOMPP E VMKLX-LERH TSGOIX SV E PIJX.

b. XLZCCFKZEV: R DRTYZEV NYZTY DRBVJ R WIVETYDRE JYILX YZJ JYFLCUVIJ NZKY XFFU IVRJFE.

c. DHKDZOT: TJPM DMMZQZMZIXZ OJRVMY HT YZDOT.

and Question 3 should be using all caps as well.

* On page 57, the final paragraph reads:

>“Just as in the reverse cipher in Chapter 5, …”

However, the reverse cipher was in chapter 4 because chapter 5 is the Caesar cipher!

* On page 84, end of the third-to-last paragraph:

>“(All the variables in the reverse cipher and Caesar cipher programs in Chapters 5 and 6, respectively, were global.)”

Chapter 6 was the Caesar cipher hacker program!

* On page 166, the fourth paragraph:

>Line 30 uses string interpolation to print the key currently being tested using string interpolation to provide feedback to the user.

* On page 236, the code block​

​

    >>> letterMapping1 = simpleSubHacker.addLettersToMapping(letterMapping1,
    'OLQIHXIRCKGNZ', candidates[0])
    >>> letterMapping1

Should be

    >>> simpleSubHacker.addLettersToMapping(letterMapping1, 'OLQIHXIRCKGNZ', candidates[0])
    >>> letterMapping1

* On page 237, the code blocks:

​

    >>> letterMapping1 = simpleSubHacker.addLettersToMapping(letterMapping1,
    'OLQIHXIRCKGNZ', candidates[1])
    >>> letterMapping1

and

    >>> letterMapping2 = simpleSubHacker.getBlankCipherletterMapping()
    >>> wordPat = makeWordPatterns.getWordPattern('PLQRZKBZB')
    >>> candidates = wordPatterns.allPatterns[wordPat]
    >>> candidates
    ['CONVERSES', 'INCREASES', 'PORTENDED', 'UNIVERSES']
    >>> for candidate in candidates:
    ...     letterMapping2 = simpleSubHacker.addLettersToMapping(letterMapping2, 'PLQRZKBZB', candidate)
    ...
    >>> letterMapping2

should be

    >>> simpleSubHacker.addLettersToMapping(letterMapping1, 'OLQIHXIRCKGNZ', candidates[1])
    >>> letterMapping1

and

    >>> letterMapping2 = simpleSubHacker.getBlankCipherletterMapping()
    >>> wordPat = makeWordPatterns.getWordPattern('PLQRZKBZB')
    >>> candidates = wordPatterns.allPatterns[wordPat]
    >>> candidates
    ['CONVERSES', 'INCREASES', 'PORTENDED', 'UNIVERSES']
    >>> for candidate in candidates:
    ...     simpleSubHacker.addLettersToMapping(letterMapping2, 'PLQRZKBZB', candidate)
    ...
    >>> letterMapping2

* On page 238, the code block:​

​

    >>> letterMapping3 = simpleSubHacker.getBlankCipherletterMapping()
    >>> wordPat = makeWordPatterns.getWordPattern('MPBKSSIPLC')
    >>> candidates = wordPatterns.allPatterns[wordPat]
    >>> for i in range(len(candidates)):
    ...     letterMapping3 = simpleSubHacker.addLettersToMapping(letterMapping3, 'MPBKSSIPLC', candidates[i])
    ...
    >>> letterMapping3

should be

    >>> letterMapping3 = simpleSubHacker.getBlankCipherletterMapping()
    >>> wordPat = makeWordPatterns.getWordPattern('MPBKSSIPLC')
    >>> candidates = wordPatterns.allPatterns[wordPat]
    >>> for i in range(len(candidates)):
    ...     simpleSubHacker.addLettersToMapping(letterMapping3, 'MPBKSSIPLC', candidates[i])
    ...
    >>> letterMapping3

# May 14, 2018 Update:

* On page 253, the code block:​

​

    >>> building = ''
    >>> for c in 'Hello world!':
    >>>     building += c
    >>> print(building)

should be

    >>> building = ''
    >>> for c in 'Hello world!':
    ...    building += c
    ...
    >>> print(building)

* On page 254, the code block:​

​

    >>> building = []
    >>> for c in 'Hello world!':
    >>>     building.append(c)
    >>> building = ''.join(building)
    >>> print(building)

should be

    >>> building = []
    >>> for c in 'Hello world!':
    ...    building.append(c)
    ...
    >>> building = ''.join(building)
    >>> print(building)

# May 15, 2018 Update

* On page 260, the last line:

>Similarly, the letters that appear least often in the ciphertext are more likely to have been encrypted from to X, Q, and Z in plaintext.

# May 18, 2018 Update

* On page 298, the code:​

​

    >>> set([1, 2, 3, 3, 4])
    set([1, 2, 3, 4])

outputs

    >>> set([1, 2, 3, 3, 4])
    {1, 2, 3, 4}

for me, but that may be the interactive shell or OS I'm using (Ubuntu 16.04 with Python 3.5.2). TODO: Can anyone else confirm?

* On page 306, the code:

​

    >>> def printStuff():
            print('Hello', end='\n')
            print('Howdy', end='')
            print('Greetings', end='XYZ')
            print('Goodbye')
    >>> printStuff()

should be

    >>> def printStuff():
    ...     print('Hello', end='\n')
    ...     print('Howdy', end='')
    ...     print('Greetings', end='XYZ')
    ...     print('Goodbye')
    ...     
    >>> printStuff()

# May 19, 2018 Update

* On page 318, the code block:

​

    >>> import secrets
    >>> otp = ''
    >>> for i in range(55):
            otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    >>> otp

should be

    >>> import secrets
    >>> otp = ''
    >>> for i in range(55):
    ...     otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    >>> otp

I think. Ubuntu 16.04 LTS doesn't have Python 3.6 or above. TODO: Can someone confirm?

* On page 326, the code block:

​

    >>> primeNum.isPrime(13)
    True

should be

    >>> primeNum.isPrime(13)
    False

Here's the thing: isPrime() checks a number for divisibility by low prime numbers (which would make it not prime). Therefore, 13 is divisible by the low prime number 13 and is not prime by that definition.

You'd have to add something like:

    if num in LOW_PRIMES:
        return True  # Low prime numbers are still prime numbers

to isPrime() to keep it from doing that.

# May 20, 2018 Update:

* On page 341 and 347, the code:

​

    64. print('The private key is a %s and a %s digit number.' %
    (len(str(publicKey[0])), len(str(publicKey[1]))))

should be

    64. print('The private key is a %s and a %s digit number.' %
    (len(str(privateKey[0])), len(str(privateKey[1]))))