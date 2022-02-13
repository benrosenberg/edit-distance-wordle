import random

# levenshtein distance

def l_dist(a, b):
    if len(b) == 0: return len(a)
    if len(a) == 0: return len(b)
    if a[0] == b[0]: return l_dist(a[1:], b[1:])

    return 1 + min(
        l_dist(a[1:], b),
        l_dist(a, b[1:]),
        l_dist(a[1:], b[1:])
    )

# [n_tries] tries to get n-letter word 
n_tries = 100

with open('words_alpha.txt', 'r') as f:
    all_words = set([l[:-1] for l in f.readlines()])

with open('5k.txt', 'r') as f: # source: https://github.com/mahsu/IndexingExercise/blob/master/5000-words.txt
    common_words = set([l[:-1] for l in f.readlines()])

words_long = [w for w in common_words if len(w) >= 5]

word = random.choice(words_long).upper()

def valid(attempt):
    attempt = attempt.lower()
    if attempt in all_words and len(attempt) >= 5:
        return True
    elif attempt in all_words:
        return 'Too short' if len(attempt) < 5 else 'Too long'
    else:
        return 'Not in dictionary'

def result(attempt, word):
    attempt = attempt.upper()
    if attempt == word:
        print('Correct!')
        return True
    if (validity := valid(attempt)) != True:
        print(validity)
        return False
    return f"edit distance {l_dist(attempt, word)} away"

tries = 0
got_it = False 
attempts = []
while tries < n_tries:
    tries += 1
    attempt = input('> ')
    out = result(attempt, word)
    if out == True:
        if tries == 1:
            print(f'It only took you one try!')    
        else:
            print(f'It only took you {tries} tries.')
        break
    elif out == False:
        tries -= 1 # don't use up a try
        continue
    else:
        attempts.append(attempt)
        print(f"{tries}/{n_tries}: " + out)
else:
    print(f'Too bad, you didn\'t get it.\nThe word was {word}.')
