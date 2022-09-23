'''import random as rndm
def play_again() -> bool:
    play_again_answer = input('Do you want to play again? Y/N ')
    if play_again_answer == 'Y':
        return True
    if play_again_answer == 'N':
        return False
    else:
        print('Sorry, try again')
        play_again()
        
def get_bank() -> int:
    bank = 1
    bank = int(input('How many chips do you wanna play with? ==> '))
    if bank < 0 :
        print('Too low a value, you can only choose 1 - 100 chips')
    elif bank > 100 :
        print('Too high a value, you can only choose 1 - 100 chips')
        get_bank()
    return bank

def get_wager(bank : int) -> int:
    user_wager = int(input('How many chips do you want to wager? ==> '))
    if get_wager > bank :
        print('The wager amount cannot be greater than how much we have.', bank,)
    elif get_wager < 0 :
        print('The wager amount must be greater than 0. Please enter again.')        
    return user_wager

def get_slot_results() -> tuple:   
    reela = rndm.randint(1,10)
    reelb = rndm.randint(1,10)
    reelc = rndm.randint(1,10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb == reelc:
        matches = 3
    elif reela == reelb and reela != reelc:
        matches = 2
    elif reelb == reelc and reelb != reela:
        matches = 2
    elif reelc == reela and reelc != reelb:
        matches = 2
    elif reela != reelb and reela != reelc and reelb != reelc:
        matches = 0
        return matches

def get_payout(wager, matches):
    if matches == 0:
        return wager * -1
    elif matches == 2:
        return wager * 3
    elif matches == 3:
        return wager * 10

if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
    while bank > 0:
        wager = get_wager(bank)
        reel1, reel2, reel3 = get_slot_results()
        matches = get_matches(reel1, reel2, reel3)
        payout = get_payout(wager, matches)
        bank = bank + payout
        print("Your spin", reel1, reel2, reel3)
        print("You matched", matches, "reels")
        print("You won/lost", payout)
        print("Current bank", bank)
        print()
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()'''

import random as rndm







def play_again() -> bool:

    play_again_answer = input('Do you want to play again? Y/N ')

    if play_again_answer == 'Y':

        return True

    if play_again_answer == 'N':

        return False

    else:

        print('Sorry, try again')

        play_again()




def get_bank() -> int:

    bank = 1

    bank = int(input('How many chips do you wanna play with? '))

    if bank < 0 or bank > 100:

        print('Sorry, try again')

        get_bank()

    return bank



def get_wager(bank : int) -> int:

    wager = bank

    user_wager = int(input('How many chips would you like to wager? '))

    if wager > bank :

        print('The wager amount cannot be greater than how much we have.', bank,)

        user_wager()

    return user_wager







def get_slot_results() -> tuple:

    reela = rndm.randint(1,10)

    reelb = rndm.randint(1,10)

    reelc = rndm.randint(1,10)

    return reela, reelb, reelc




def get_matches(reela, reelb, reelc) -> int:

    if reela == reelb == reelc:

        matches = 3

    elif reela == reelb and reela != reelc:

        matches = 2

    elif reelb == reelc and reelb != reela:

        matches = 2

    elif reelc == reela and reelc != reelb:

        matches = 2

    elif reela != reelb and reela != reelc and reelb != reelc:

            matches = 0

            return matches




def get_payout(wager, matches):

    if matches == 0:

        return wager * -1

    elif matches == 2:

        return wager * 3

    elif matches == 3:

        return wager * 10







if __name__ == "__main__":

    playing = True

    while playing:

        bank = get_bank()

        while bank > 0:

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)

            payout = get_payout(wager, matches)

            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)

            print("You matched", matches, "reels")

            print("You won/lost", payout)

            print("Current bank", bank)

            print()

            print("You lost all", 0, "in", 0, "spins")

            print("The most chips you had was", 0)

            playing = play_again()
