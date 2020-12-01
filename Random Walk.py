# import libraries
import matplotlib.pyplot as plt
from random import choice

# let's define a function

def random_walk(num_steps):
    walk = [] # create en empty list
    first_choice = choice([1,-1]) # we move either up or down
    walk.append(first_choice) # add it to the list
    for i in range(1,num_steps): # we're going to move between 1 and the number of steps we entered in the function
        next_choice = choice([1,-1]) # we have to choose either up or down again
        next_step = walk[i-1] + next_choice # give another step which is the previous one plus the new choice
        walk.append(next_step) # append the new step to the list and the loop starts over again
    return walk

def plot_random_walk(walk):
    x = list(range(1,len(walk)+1)) # define x as the walk distance

    plt.plot(x,walk) # plot both variables
    plt.xlabel('Walk distance')
    plt.ylabel('Random walk')
    plt.title('Our Random Walk')
    plt.show()
