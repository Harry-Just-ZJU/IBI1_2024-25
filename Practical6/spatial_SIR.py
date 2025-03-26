 
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import viridis

# make array of all susceptible population (use the code in the Practical6 pdf)
population = np.zeros((100, 100))

# randomly select the outbreak point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# draw figure (when outbreak begins)
plt.figure(figsize = (6, 4), dpi = 150)
plt.imshow(population, cmap = viridis, interpolation = 'nearest')
plt.title('at times 0')
plt.show()

# define basic concept
beta = 0.3
gamma = 0.05

# loop for 100 times from 1
for t in range(1, 101):
    # create a copy in the loop environment
    new_population = population.copy()

    # find all the (x, y) of the infected point
    rows, cols = np.where(population == 1)

    # go through every infected person
    for i in range(len(rows)):
        row = rows[i]
        col = cols[i]

        # recover
        if np.random.rand() < gamma:
            new_population[row, col] = 2

        # infect
        for x_dis in [-1, 0, 1]:
            for y_dis in [-1, 0, 1]:

                # except the point itself
                if x_dis == 0 and y_dis == 0:
                    continue

                # get to the every point surrounded
                new_row = row + x_dis
                new_col = col + y_dis

                # judge whether the point surrounded is outside the 100 * 100 array and is still susceptible
                if 0 <= new_row < 100 and 0 <= new_col < 100 and new_population[new_row, new_col] == 0:
                    if np.random.rand() < beta:
                        new_population[new_row, new_col] = 1
    # update
    population = new_population

    # draw figure according to the guidance
    if t in [10, 50, 100]:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = viridis, interpolation = 'nearest')
        plt.title('at times ' + str(t))
        plt.show()