from random import *
def main():
    kids = generateRandomKids(2,4)

def generateRandomKids(numberOfKids,numberOfBits):
    kids = []
    genKid = lambda n: [randint(0,1) for b in range(0,numberOfBits)]
    for i in range(numberOfKids):
        kids.append(genKid(numberOfBits))
    return kids
if __name__ == "__main__":
    main()