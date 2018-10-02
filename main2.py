import random
import time
from itertools import product


def cmp_guess(guess, master):
    black_pegs = 0
    white_pegs = 0

    not_matches_guess = []
    not_matches_master = []

    for i in range(len(guess)):
        if guess[i] == master[i]:
            black_pegs += 1
        else:
            not_matches_guess.append(guess[i])
            not_matches_master.append(master[i])

    for color in set(not_matches_master):
        if color in not_matches_guess:
            white_pegs += 1

    return black_pegs, white_pegs


def main():
    code_length = 4
    color_str = 'rgboyp'
    max_guesses = 12

    master = ''
    for i in range(code_length):
        master += random.choice(color_str)

    all_codes = set(product(color_str, repeat=code_length))
    s = all_codes.copy()
    guess = 'rrgg'

    for i in range(max_guesses, 0, -1):
        print('\n{} round(s) remaining:'.format(i))

        print('Jaquelin> thinking.', end='')
        time.sleep(0.5)
        print('\rJaquelin> thinking.', end='')
        time.sleep(0.5)
        print('\rJaquelin> thinking..', end='')
        time.sleep(0.5)
        print('\rJaquelin> thinking...', end='')
        time.sleep(0.5)
        print('\rJaquelin> Guessing [{}]'.format(''.join(guess)))
        time.sleep(1)

        pegs = cmp_guess(guess, master)
        print('Black Pegs: {}\nWhite Pegs: {}'.format(pegs[0], pegs[1]))

        if pegs[0] == code_length:
            print('You Win!')
            return

        # Knuth's Algorithm
        to_remove = set([])
        for code in s:
            if cmp_guess(guess, code) != pegs:
                to_remove.add(code)
        s.difference_update(to_remove)

        max_score = 0
        best_guesses = set([])
        for guess_candidate in all_codes:
            peg_categories = {}
            for elem in s:
                peg_test = cmp_guess(guess_candidate, elem)
                if peg_test not in peg_categories:
                    peg_categories[peg_test] = 0

                peg_categories[peg_test] += 1

            if peg_categories.values():
                score = len(s) - max(peg_categories.values())
            else:
                score = len(s)

            if score == max_score:
                best_guesses.add(guess_candidate)
            elif score > max_score:
                max_score = score
                best_guesses = {guess_candidate}

        try:
            guess = next(iter(best_guesses.intersection(s)))
        except StopIteration:
            guess = next(iter(best_guesses))

        time.sleep(1)

    print('\nGame Over.\nThe master code was [{}]\nYou Lose!'.format(master))


if __name__ == '__main__':
    main()
