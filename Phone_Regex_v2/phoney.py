import re

def clean_phone_numbers(numbers):
    # TODO: Create a function that accepts a list of strings and returns a list that consists of valid 10-digit North American phone numbers
    for i in range(len(numbers)):
        clean = ''
        for num in numbers[i]:
            if num in '0123456789':
                clean += num
        numbers[i] = clean
    
    #for i in range(len(numbers)):
        #cleanStrings = "".join(c for c in numbers[i] if c in '0123456789')
    
    #superClean = "".join(s for s in numbers if len(cleanStrings) == 10)'''

    j = len(numbers) - 1
    while j >= 0:
        if len(numbers[j]) != 10:
            del numbers[j]
        j -= 1
    
    
    cleanNumbers = []
    cleanNumbers = [cnum for cnum in numbers if re.search(r"(\b[^0|1]\d{2})[^0|1]\d{2}\d{4}\b", cnum)]
    clean = []
    clean = [nnum for nnum in cleanNumbers if re.search(r"\b\d{3}(?!555)\d{4}", nnum)]
    #print(f"{len(cleanNumbers)} valid phone numbers were found.")
    print(f"{len(clean)} valid phone numbers were found.")
    return clean

def find_number(numbers: list, search_term: str):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not th appears in the list
    # This function searches for an entire US phone number
    count = 0
    match = []
    for x in numbers:
        if x == search_term:
            count += 1
            match.append(x)

    print(f"The phone number was found {count} times in the list of phone numbers: ['{match}']")



def find_areacode(numbers: list, search_term: str):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not th appears in the list
    # This function searches for the area code of a phone number
    count = 0
    match = []
    for x in numbers:
        if x[0:3] == search_term:
            count += 1
            match.append(x)

    print(f"The phone number was found {count} times in the list of phone numbers: ['{match}']")



def find_exchange(numbers: list, search_term: str):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not th appears in the list
    # This function searches for the exchange of a phone number
    
    count = 0
    match = []
    for x in numbers:
        if x[3:6] == search_term:
            count += 1
            match.append(x)
    
    '''results = [num for num in numbers if num[3:6] == search_term]
    print(f"\nThe phone number was found {len(results)} times in the list of phone numbers.: {results}\n")
    return results'''

    print(f"The phone number was found {count} times in the list of phone numbers: ['{match}']")

