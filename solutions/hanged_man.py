from random import choice

words = [
    "impartial",
    "imperfect",
    "impolite",
    "imperative",
    "speculative",
    "cumulative"
]

# Here we pickup the secret word to be guessed
secret_word = choice(words).lower()
displayed_word = len(secret_word)*'_'
max_attempts = 13


def input_letter():
    """
    Requests the user to type a letter. Loop until a single letter is actually entered
    :return: a single letter (str) typed by the user
    """
    while True:
        answer = input("Quelle lettre voulez-vous dévoiler ? ")
        if len(answer) != 1 or len(answer) == 1 and answer[0] not in "abcdefghijklmnopqrstuvwxyz":
            print("Cette entrée est incorrecte, veuillez recommencer")
        else:
            return answer

def replace(letter, original_word, hidden_word):
    """
    Find all appearances of a letter in an original word and replace the character with the same index in a hidden word
    :param letter: the letter to be searched for
    :param original_word: the word in which the function searches for positions
    :param hidden_word: the word in which positions of the letter found it the original word are replaced by the letter itself
    :return: the updated hidden word
    """
    new_displayed_word = ""
    for i, l in enumerate(original_word):
        if l == letter or hidden_word[i] != "_":
            new_displayed_word += l
        else:
            new_displayed_word += "_"
    return new_displayed_word


# Start playing!
for i in range(max_attempts):
    print("Il vous reste", 12-i, "coup" + "s" if max_attempts-i > 0 else "")
    print(displayed_word.upper())
    letter = input_letter().lower()
    displayed_word = replace(letter, secret_word, displayed_word)
    if '_' not in displayed_word:
        print("Bravo, vous avez gagné en", max_attempts-i, "coups !")
        break

print("Désolé, c'est perdu, le mot était", secret_word)