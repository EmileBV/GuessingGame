from random import randint

charsets = {
    "A" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "0" : "0123456789",
    "X" : "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}

allowed_pattern = "".join(charsets.keys())

def match_pattern(to_check: str, pattern: str):
    for i in range(len(pattern)):
        if not to_check[i] in charsets[pattern[i]]:
            return False
    return True


print("Please enter the pattern of the secret string")
print("A : Alphabetical")
print("0 : Numeral")
print("X : Alphanumeric")
print("Example: AA0000")
pattern = input().upper()

if all([c in allowed_pattern for c in pattern]):
    print("Pattern is valid!")
else:
    print("Pattern is invalid!")
    quit()

print("Please enter max tries")
max_tries = int(input())

secret = "".join([charsets[c][randint(0, len(charsets[c])-1)] for c in pattern])

win = False
tries = 0

while not win and tries < max_tries:
    print("")
    print(f"Please enter your guess. Remaining tries: {max_tries - tries}. (Pattern is {pattern})")
    guess = input().upper()
    if len(guess) != len(pattern):
        print("The length of the string was wrong, try again")
    elif not match_pattern(guess, pattern):
        print("guess doesn't match pattern, try again")
    else:
        tries += 1
        if guess == secret:
            win = True
        else:
            good = 0
            perfect = 0
            for i in range(len(guess)):
                if guess[i] in secret:
                    good += 1
                    if guess[i] == secret[i]:
                        perfect += 1
            print(f"Correct : {good}")
            print(f"In right position: {perfect}")

if win:
    print("Congrats you won!")
else:
    print("You lost, better luck next time.")

print(f"tries: {tries}")
print(f"The secret string was: {secret}")
