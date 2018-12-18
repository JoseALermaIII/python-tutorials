"""All my cats 2.0

This program efficiently showcases your cats by using a list to store the cat's names
and a while loop to prompt for them. Then, using a for loop on the list to print them
all.

"""


def main():
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) +
              ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name]  # list concatenation
    print('The cat names are:')
    for name in catNames:
        print('  ' + name)


if __name__ == "__main__":
    main()
