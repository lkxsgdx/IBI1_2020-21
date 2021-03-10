# An r rate of 1.2 means that each infected individual will on average infect 1.2 individuals.	
r = 1.2
# "n" means the number of IBI1 students.
n = 84
# "N" means the number of infected indivuduals after 5 rounds of infection.
N = n * (1.2 ** 5)
print("the number of infected indivuduals after 5 rounds of infection is", N)
