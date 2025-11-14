import random

def fitness(individual):
    ones = individual.count('1')
    if ones == 50:
        return 80
    else:
        return 80 - abs(50 - ones)

population_size = 300
chromosome_length = 80

def generate_individual():
    return ''.join(random.choice(['0', '1']) for _ in range(chromosome_length))

population = [generate_individual() for _ in range(population_size)]

def selection(pop):
    selected = []
    for _ in range(len(pop)):
        a = random.choice(pop)
        b = random.choice(pop)
        selected.append(a if fitness(a) > fitness(b) else b)
    return selected

def crossover(p1, p2):
    point = random.randint(1, chromosome_length - 1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2

mutation_rate = 0.01

def mutate(ind):
    bits = []
    for b in ind:
        if random.random() < mutation_rate:
            bits.append('0' if b == '1' else '1')
        else:
            bits.append(b)
    return ''.join(bits)

generations = 50

for g in range(generations):
    selected = selection(population)
    next_population = []

    for i in range(0, population_size, 2):
        p1 = selected[i]
        p2 = selected[i+1]
        c1, c2 = crossover(p1, p2)
        next_population.append(mutate(c1))
        next_population.append(mutate(c2))
    
    population = next_population

    best = max(population, key=fitness)
    print(f"Generation {g+1}: Best Fitness = {fitness(best)}")

best = max(population, key=fitness)
print("Best Individual:", best)
print("Number of Ones:", best.count('1'))
print("Final Fitness:", fitness(best))
