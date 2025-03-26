
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#  define the basic variables of the model 
N = [10000]
infected = [1]
recovered = [0]
susceptible = [N[0] - infected[0] - recovered[0]]
beta = 0.3
gamma = 0.05

# loop for 1000 times
for i in range(1, 1000):

    rd_1 = np.random.choice(range(2), infected[i - 1], p = [1 - gamma, gamma])
    num_recovered = sum(rd_1)

    pro_infect = beta * infected[i - 1] / N[0]
    rd_2 = np.random.choice(range(2), susceptible[i - 1], p = [1 - pro_infect, pro_infect])
    num_infected = sum(rd_2)

    # update
    infected.append(infected[i - 1] + num_infected - num_recovered)
    recovered.append(recovered[i - 1] + num_recovered)
    susceptible.append(susceptible[i - 1] - num_infected)

# draw figure
plt.figure(figsize = (6, 4), dpi = 150)

x = range(len(susceptible))
plt.plot(x, susceptible, label = 'susceptible')
plt.plot(x, infected, label = 'infected')
plt.plot(x, recovered, label = 'recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig('SIR model', format = 'png')        # 'type' is wrong, it should be 'format'
plt.show()