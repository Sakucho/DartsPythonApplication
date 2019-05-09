
import random

def board_to_point(s):

    n_fold = s[0]
    point = int(s[1:])

    if n_fold == 'S':
        return point * 1 
    elif n_fold == 'D':
        return point * 2 
    elif n_fold == 'T':
        return point * 3 


if __name__ == '__main__':

    darts_board = [ 20,  1, 18,  4, 13,  6, 10, 15,  2, 17,
                     3, 19,  7, 16,  8, 11, 14,  9, 12,  5]

    n_fold = ['S', 'D', 'T']

    log = []
    score = 0

    for i in range(3):
        log.append( random.choice(n_fold) + str(random.choice(darts_board)))
        score += board_to_point(log[i])

    print(log)
    
    result = input()

    print (str(score))

