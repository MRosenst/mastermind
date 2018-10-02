import random


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

    for i in range(max_guesses, 0, -1):
        print('{} round(s) remaining:'.format(i))

        guess = input()
        while len(guess) != code_length or not set(guess).issubset(set(color_str)):
            guess = input('That input is invalid. Please try again:\n')

        pegs = cmp_guess(guess, master)
        print('Black Pegs: {}\nWhite Pegs: {}'.format(pegs[0], pegs[1]))

        if pegs[0] == code_length:
            print('You Win!')
            return

    print('\nGame Over.\nThe master code was [{}]\nYou Lose!'.format(master))


if __name__ == '__main__':
    main()
