import random

def assign_doors():
    prizeInd = random.randint(0,2)
    for i in range(3):
        if(i==prizeInd):
            doors[i] = 1
        else:
            doors[i] = 0
    return(prizeInd)

def gen_first_guess():
    return(random.randint(0,2))

def reveal_empty(first_guess, prize_ind):
    toReveal = -1
    for i in range(len(doors)):
        if(i!=first_guess and i!=prize_ind):
            toReveal = i
    return(toReveal)
    
def gen_second_guess(initial_guess, host_elim):
    secReturn = -1
    for i in range(len(doors)):
        if(i!=initial_guess and i!=host_elim):
            secReturn = i
    return secReturn

# Will treat like concurrent parallel universes, with only discrepancy being the choice of the person.
# A will take offer to change guess after empty door is revealed. B will not, retaining the initial choice.
doors_prize_val = [0,0,0]
iter_to_run = int(input('\n\nEnter how many rounds to run for the simulation: '))
a_correct_guesses = 0
b_correct_guesses = 0
doors = [0,0,0]

for i in range(iter_to_run):
    prize_door = assign_doors()
    a_first = gen_first_guess()
    b_final = a_first
    
    host_bad_door_reveal = reveal_empty(a_first, prize_door)
    a_second = gen_second_guess(a_first, host_bad_door_reveal)
    if(a_second == prize_door):
        a_correct_guesses += 1
    if(b_final == prize_door):
        b_correct_guesses += 1

print("\nPerson A who took offer to repick door guessed correctly " + str(a_correct_guesses) + "/" + str(iter_to_run) + " times.\n")
print("Person B who took offer to repick door guessed correctly " + str(b_correct_guesses) + "/" + str(iter_to_run) + " times.\n")
