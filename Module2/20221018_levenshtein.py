#from levenshtein import distance
import Levenshtein
import random

gv_objects = []
gv_playerscore = 0
gv_computerscore = 0

def clean_guess(iv_guess, iv_objects):
    lv_list = [Levenshtein.distance(iv_guess, iv_objects[0]),
               Levenshtein.distance(iv_guess, iv_objects[1]),
               Levenshtein.distance(iv_guess, iv_objects[2])]
    lv_min = lv_list.index(min(lv_list))
    return iv_objects[lv_min]

def main():
    print('Please enter the 3 objects you want to play the game with:')
    lv_object = str(input('Object 1 (beats object 2):'))
    gv_objects.append(lv_object)
    lv_object = str(input('Object 2 (beats object 3):'))
    gv_objects.append(lv_object)
    lv_object = str(input('Object 3 (beats object 1):'))
    gv_objects.append(lv_object)
    gv_escape = str(input('Game ends with this word: :'))
    print(gv_objects)
    print('Game begins !')
    gv_playerscore = 0
    gv_computerscore = 0
    gv_guess  = str(input('Please enter your guess:'))
    while gv_guess != gv_escape:
        gv_guess = clean_guess(gv_guess, gv_objects)
        gv_computer = random.choice(gv_objects)

        if ( ( gv_guess == gv_objects[0] and gv_computer == gv_objects[1] ) or
             ( gv_guess == gv_objects[1] and gv_computer == gv_objects[2] ) or
             ( gv_guess == gv_objects[2] and gv_computer == gv_objects[0] )):
            gv_playerscore += 1
        elif ( ( gv_computer == gv_objects[0] and gv_guess == gv_objects[1] ) or
               (gv_computer == gv_objects[1] and gv_guess == gv_objects[2]) or
               ( gv_computer == gv_objects[2] and gv_guess == gv_objects[0] )):
            gv_computerscore += 1

        print(gv_guess, gv_computer, gv_escape)
        print(gv_playerscore, gv_computerscore)

        gv_guess = str(input('Please enter your guess:'))

    if gv_playerscore > gv_computerscore:
        print(f"{gv_playerscore}-{gv_computerscore} You won. Congratulations!")
    elif gv_computerscore > gv_playerscore:
        print(f"{gv_playerscore}-{gv_computerscore} I won. Want to play again ?")
    else:
        print(f"{gv_playerscore}-{gv_computerscore} Draw. Want to play again ?")

if __name__ == "__main__":
    main()