'''
goal : find the guessed number via genetic algorithm

-> Generation = ne iteration of population
  -> population = n chromosomes
    -> chromosome = guessed = n digits
      -> digit = [0 .. 9]
      -> gene = one digit of the guessed

-> fitness of chromosome
  -> digitwise compare with actual guessed

-> parents
  -> taken of the fittest of generation

-> crossover fittest
  -> random n digits from parent1 and n digits from parent2 (n+n = length of chromosome)

-> mutation
  -> to avoid local convergence
  -> probabilistic basis i.e 10% of children
  -> randomn gene of child to randomn digit 
'''
import numpy as np
import random
from random import randrange

population_amount = 10
parent_amount = 5
elite_amount = 2

#print(population)    

def fitness(population):
  fitnesses = []
  for chromosome in population:
    fitness_chro = 0
    for i in range(len(chromosome)):
      #print(i)
      if chromosome[i] == to_guess[i]:
        fitness_chro += 1
    pair = [chromosome, fitness_chro]    
    fitnesses.append(pair)
  return fitnesses  

#print(fitness(population))

def fittest(population):
  return sorted(population, key=lambda x: x[1], reverse = True)[:parent_amount]

def parents(fitnesses):
  final_parents = []
  fittest_parents = fittest(fitnesses)
  
  for i in range(parent_amount):
    final_parents.append((fittest_parents[i])[0])

  return final_parents 

#print(parents(population))


def crossover(p1, p2):
  child = []
  gene1 = int(random.random() * to_guess_length)
  gene2 = int(random.random() * to_guess_length)

  i_start = min(gene1, gene2)
  i_end = max(gene2, gene1)

  #print("i_start: " + str(i_start))
  #print("i_end: " + str(i_end))


  for i in range(0,to_guess_length):
    #print(i)
    if (i < i_start) or (i > i_end):
      child.append(p1[i])
    else:
      child.append(p2[i])

  return child

def breeding(parents):
  children = []
  children_amount = len(population) - elite_amount

  for i in range(0,elite_amount):
    children.append(parents[i])

  for i in range(children_amount):
    i_1 = int(random.random() * len(parents))
    i_2 = int(random.random() * len(parents))

    p1 = parents[i_1]
    p2 = parents[i_2]

    children.append(crossover(p1,p2))

  return children

def mutation(children):
  children[len(children)-1][randrange(to_guess_length)] = randrange(10)
    
  return children 

#print(population)
#print(mutation(population))

# main

current = [None, None]
generation = 0

to_guess = [int(i) for i in str(input("number to guess: "))]
#print(to_guess)
to_guess_length = len(to_guess)

fitness_index = 0

population = []
for i in range(population_amount):
    chromosome = []
    for x in range(to_guess_length):
        chromosome.append(randrange(10))
    population.append(chromosome)

print(population)

while to_guess != current[0]:
  fitnesses = fitness(population)
  current = fittest(fitnesses)[0]
  #print("fitness local: " + str(current[1]))
  parent = parents(fitnesses)
  children = breeding(parent)
  population = mutation(children)
  #print(type(current[1]))
  #if fitness_index < current[1]:
  print("generation: " + str(generation))
  print("to guess: " + str(to_guess))
  print("current: " + str(current))
  #fitness_index = fittest(fitnesses)[1]
  generation += 1
  





