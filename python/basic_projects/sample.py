import random
import sys


HANGMAN_ASCII = ["------------------", 
               "|        |        ", 
               "|        0        ", 
               "|       /|\\       ", 
               "|        |        ", 
               "|       / \\       ", 
               "|                 "]
HANGMAN_LEN = len(HANGMAN_ASCII)


def display_hangman(count: int = HANGMAN_LEN):
    if count > len(HANGMAN_ASCII) or count < 0:
        print("Ooops wrong number")
        sys.exit(1)

    for i in range(count):
        print(HANGMAN_ASCII[i])


def fill_answer(target: str, c: str):
    pass


def get_question():
    """Randomly return a string of target word from a list"""
    questions = ["bird", "racecar", "apple", "banana", "python", "wolf"]
    upper_bound = len(questions) - 1
    rand_index = random.randint(0, upper_bound)
    return questions[rand_index]


def check_answer(target: str, c: str):
    return c.upper() in target.upper()


def display_placeholder(target: str):
    l = len(target)
    for i in range(l):
        print(" [ ] ", end="")
    print("")


def display_word_target(q: str, target: list, c: str):
    l = len(target)
    for i in range(l):
        if c.upper() == q[i].upper():
            target[i] = c.upper()
            print(f" {c} ", end="")
        elif target[i] != "_":
            print(f" {target[i]} ", end="")
        else:
            print(" [ ] ", end="")
    print("")


def get_user_answer():
    """Get user answer from standard input"""
    user_answer = input("> ")
    return user_answer


def word_contains(word: str, c: str):
    return c in word


def main():
    """Main driver function"""
    player_win = False
    player_lose = False
    hangman_count = 0
    q = get_question()
    q_prog = list("_") * len(q)
    display_placeholder(q)
    while True:
        display_hangman(hangman_count)
        print()
        a = get_user_answer()[0].upper()
        if not check_answer(q, a):
            hangman_count += 1
        display_word_target(q, q_prog, a)
        print()
        if hangman_count == HANGMAN_LEN:
            player_lose = True
            break
        if "_" not in q_prog:
            player_win = True
            break

    if player_lose:
        print("YOU LOSE!")
        return
    print("YOU WIN")



if __name__ == "__main__":
    main()
