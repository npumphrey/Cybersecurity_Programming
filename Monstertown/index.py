from monstertown import Town, Monster, Vampire, Mutant
import random


def main():
    # TODO: Make some towns and monsters

    godzilla = Mutant("Godzilla", 40.2, 23000)

    muncie = Town("Muncie", random.randint(10000, 50000), random.randint(100, 2000), random.randint(50, 1000))
    indianapolis = Town("Indianapolis", random.randint(10000, 50000), random.randint(100, 2000), random.randint(50, 1000))
    carmel = Town("Carmel", random.randint(10000, 50000), random.randint(100, 2000), random.randint(50, 1000))
    zionsville = Town("Zionsville", random.randint(10000, 50000), random.randint(100, 2000), random.randint(50, 1000))
    greenwood = Town("Greenwood", random.randint(10000, 50000), random.randint(100, 2000), random.randint(50, 1000))

    indiana = [muncie, indianapolis, carmel, zionsville, greenwood]

    print(muncie.describe_town())
    print(indianapolis.describe_town())
    print(carmel.describe_town())
    print(zionsville.describe_town())
    print(greenwood.describe_town())
    print("\n")

    # megalon = Monster("Megalon", 34.3, 9400)

    # print(megalon.say_hello())

    # print(megalon.describe_activity())

    # muncie = megalon.terrorize_town(muncie)
    # print(megalon.describe_activity())
    # print(muncie.describe_town())

    # vladimir = Vampire("Vladimir", 2.5, 170)
    # print(vladimir.say_hello())

    # muncie = vladimir.terrorize_town(muncie)
    # print(vladimir.describe_activity())
    # print(muncie.describe_town())
    
    # godzilla = Mutant("Godzilla", 40.2, 23000)
    
    # muncie = godzilla.terrorize_town(muncie)
    # print(muncie.describe_town())

    # muncie = godzilla.terrorize_town(muncie)
    # print(muncie.describe_town())
    
    # muncie = godzilla.terrorize_town(muncie)
    # print(muncie.describe_town())

    rampage_num = 1
    while rampage_num <= 3:
        print(f"Rampage number {rampage_num}!")
        godzilla.rampage(indiana)
        print("\n")
        rampage_num += 1


if __name__ == '__main__':
    main()