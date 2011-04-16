#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aaron
#
# Created:     16Apr2011
# Copyright:   (c) aaron 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
from binaryArray_chromosome import *

def main():
    # set default values
    max_generations = 100
    chromosome_size = 128
    population_size = 100
    # override defaults with command-line input (if it exists)
    for i in sys.argv:
        arg = i.split('=')
        if arg[0] == 'gens':
            max_generations = int(arg[1])
        elif arg[0] == 'length':
            chromosome_size = int(arg[1])
        elif arg[0] == 'popsize':
            population_size = int(arg[1])
        elif arg[0] == 'mutrate':
            Chromosome.mutation_rate = float(arg[1])

    # document what we're doing
    print("Starting search for a {}-length array over {} generations with a "
    "population size of {} and a mutation rate of {}%".format(chromosome_size,
    max_generations, population_size, Chromosome.mutation_rate*100))

    # generate the initial population
    population = [Chromosome(chromosome_size) for i in range(population_size)]
    # store the population as a list of tuples where each tuple contains a
    #  chromosome and its fitness score
    population = list(zip(population, map(lambda chr: chr.get_fitness(), population)))
    # run the solver the specified # of generations, outputting the
    #  the best solution after each run
    for i in range(max_generations):
        # sort by fitness
        population.sort(key=lambda item: item[1], reverse=True)

        # output our progress so far
        # print("generation: {}\nBest: {}\nFitness: {}".format(i, population[0][0].data, population[0][1]))
        print("generation: {}\t best: {}".format(i, population[0][1]))

        # if we've already reached max score, stop searching
        if population[0][1] == chromosome_size:
            break

        # kill the poor performers
        population = population[:len(population)//2]

        # reproduce, which has mutation built in
        children = []
        for j in range(0, len(population) - 1, 2):
            first, second, pivot = Chromosome.reproduce(population[j][0], population[j+1][0])
            children.extend([(first, first.get_fitness()), (second, second.get_fitness())])
        population.extend(children)

if __name__ == '__main__':
    main()