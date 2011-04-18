#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aaron
#
# Created:     17/04/2011
# Copyright:   (c) aaron 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import math
import random
from graphics import *
from tsp_chromosome import *

def select_parents(population):
    # get parents based on a tournament selection
    # choose 5 parents at random
    # return the best 2
    return sorted(random.sample(population, 5), key=lambda item: item[1])[:2]

def main():
    # set default values
    max_generations = 160
    cities = 45
    population_size = 150
    # override defaults with command-line input (if it exists)
    for i in sys.argv:
        arg = i.split('=')
        if arg[0] == 'gens':
            max_generations = int(arg[1])
        elif arg[0] == 'cities':
            cities = int(arg[1])
        elif arg[0] == 'popsize':
            population_size = int(arg[1])
        elif arg[0] == 'mutrate':
            Chromosome.mutation_rate = float(arg[1])

    # document what we're doing
    print("Starting search for the optimal path through {} cities over {} generations with a "
    "population size of {} and a mutation rate of {}%".format(cities,
    max_generations, population_size, Chromosome.mutation_rate*100))

    # lay out the cities in a 2d plane (500x500)
    positions = []
    angle_increment = 2*math.pi / cities
    base_dist = 240
    dist_offset = -250
    for i in range(cities):
        angle = i * angle_increment
        x = base_dist * math.sin(angle) - dist_offset
        y = base_dist * math.cos(angle) - dist_offset
        positions.append(Point(x, y))

    # determine the distances from each point to each other point
    for i, src in enumerate(positions):
        for j, dst in enumerate(positions):
            Chromosome.distances[(i, j)] = None if i == j else math.sqrt((src.x - dst.x)**2 + (src.y - dst.y)**2)
            #print(Chromosome.distances[(i, j)])

    # draw the window
##    win = GraphWin("TSP", 500, 500)
##    for pos in positions:
##        cir = Circle(pos, 5)
##        cir.setFill("red")
##        cir.setOutline("red")
##        cir.draw(win)
##    win.flush()

    # generate the initial population
    population = [Chromosome(cities) for i in range(population_size)]
    # store the population as a list of tuples where each tuple contains a
    #  chromosome and its fitness score
    population = list(zip(population, map(lambda chr: chr.get_fitness(), population)))
    # sort by fitness
    population.sort(key=lambda item: item[1])

    # run the solver the specified # of generations, outputting the
    #  the best solution after each run
    for i in range(max_generations):
        # output our progress so far
        print("generation: {}\t best: {}".format(i, population[0][1]))

        # reproduce, which has mutation built in
        children = []
        for i in range(population_size // 2):
            father, mother = select_parents(population)
            first, second = Chromosome.reproduce(father[0], mother[0])
            children.extend([(first, first.get_fitness()), (second, second.get_fitness())])
        population.extend(children)

        # sort by fitness
        population.sort(key=lambda item: item[1])
        # only let the strong survive
        population = population[:population_size]


##    win.getMouse()
##    win.close()

    # draw the window
    win = GraphWin("TSP", 500, 500)
    for pos in positions:
        cir = Circle(pos, 5)
        cir.setFill("red")
        cir.setOutline("red")
        cir.draw(win)

    winner = population[0][0]
    src = winner.data[0]
        # this loop will give us all edges, including the end back to the
        #  beginning (which is why we have the weird loop target)
    for dst in winner.data[1:] + winner.data[:1]:
        l = Line(positions[src], positions[dst])
        l.draw(win)
        src = dst

    win.flush()
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()