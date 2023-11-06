def inc_sqrt(n):
    guess=1
    while(guess*guess<=n):
        square = guess*guess
        if square == n:
            print(f"Guess: {guess}")
            print(f"Square Root of {n} is {guess}")
            return square
        
        guess +=1
    return -1
    
inc_sqrt(15)