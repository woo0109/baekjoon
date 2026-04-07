while True:
    password = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if password == 'end':
        break

    is_vowel = any(v in password for v in vowels)

    is_triple = False
    for i in range(len(password) - 2):
        sub = password[i:i+3]

        if all(char in vowels for char in sub) or all(char in consonants for char in sub):
            is_triple = True
            break
            
    is_double = False
    for i in range(len(password) - 1):
        sub = password[i:i+2]

        if sub[0] == sub[1]:
            if sub not in ("ee", "oo"):
                is_double = True
                break

    if not is_vowel or is_triple or is_double:
        print(f"<{password}> is not acceptable.")
    else:
        print(f"<{password}> is acceptable.")
