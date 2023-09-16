from monstertown import Town, Monster, Vampire, Mutant


def main():
    # TODO: Make some towns and monsters

    muncie = Town("Muncie", 13000, 2000, 750)

    print(muncie.describe_town())

    megalon = Monster("Megalon", 34.3, 9400)

    print(megalon.say_hello())

    print(megalon.describe_activity())

    muncie = megalon.terrorize_town(muncie)
    print(megalon.describe_activity())
    print(muncie.describe_town())

    vladimir = Vampire("Vladimir", 2.5, 170)
    print(vladimir.say_hello())

    muncie = vladimir.terrorize_town(muncie)
    print(vladimir.describe_activity())
    print(muncie.describe_town())
    
    godzilla = Mutant("Godzilla", 40.2, 23000)
    
    muncie = godzilla.terrorize_town(muncie)
    print(godzilla.describe_activity())
    print(muncie.describe_town())

    muncie = godzilla.terrorize_town(muncie)
    print(godzilla.describe_activity())
    print(muncie.describe_town())
    
    muncie = godzilla.terrorize_town(muncie)
    print(godzilla.describe_activity())
    print(muncie.describe_town())


if __name__ == '__main__':
    main()