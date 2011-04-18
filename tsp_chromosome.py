#-------------------------------------------------------------------------------
# Name:        tsp_chromosome
# Purpose:
#
# Author:      aaron
#
# Created:     17/04/2011
# Copyright:   (c) aaron 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random

class Chromosome(object):
    '''represents a potential solution for a traveling-salesman problem'''

    mutation_rate = .15

    '''the distances are represented by a dictionary; each key is a tuple in the
    form (source, destination), and the key is the distance between them'''
    distances = {} # = {(i, j):(1 if i != j else None) for i in range(25) for j in range(25)}

    def __init__(self, length=25, randomize=True):
        '''initializes an instance

        Optional 'length' argument specifies the length of the chromosome (the
        number of cities); default value is 25.

        Optional 'randomize' argument determines whether the solution is
        randomized; default value is True.'''

        self.length = length
        self.data = list(range(self.length))
        if randomize:
            random.shuffle(self.data)

    def __get_random_endpoints__(self):
        '''Returns a tuple containing a random start- and
        end-point within the chromosome'''
        p1 = random.randint(0, self.length - 1)
        p2 = p1
        # make sure they are unique
        while p2 == p1:
            p2 = random.randint(0, self.length - 1)
        # swap them so the lower value is first
        return (p1, p2) if p1 < p2 else (p2, p1)

    def reproduce(father, mother):
        '''Creates two offspring from the specified parents
        using Order Crossover Recombination'''
        # get end-points
        start, end = father.__get_random_endpoints__()
        # create two children, using both parents in each role
        return Chromosome.__reproduce__(father, mother, start, end), \
            Chromosome.__reproduce__(mother, father, start, end)

    def __reproduce__(father, mother, start, end):
        '''Creates a single child from the specified parents
        using Order Crossover Recombination'''
        # copy the segment from the first parent
        child_data = father.data[start:end]
        # add remaining data from second parent in the order it appears
        #  after the second end-point
        for i in mother.data[end:] + mother.data[:end]:
            if i not in child_data:
                child_data.append(i)
        # create a new chromosome from that data
        c = Chromosome(father.length)
        c.data = child_data
        c.__mutate__()
        return c

    def __mutate__(self):
        '''Randomly determines whether a mutation should occur and,
        if so, mutates the chromosome using Inversion Mutation'''
        if random.random() > Chromosome.mutation_rate:
            # don't mutate, just quit
            return
        # choose two unique end-points
        start, end = self.__get_random_endpoints__()
        # reverse the segment between end-points
        self.data = self.data[:start] + self.data[start:end][::-1] + self.data[end:]
        return start, end

    def get_fitness(self):
        distance = 0
        src = self.data[0]
        # this loop will give us all edges, including the end back to the
        #  beginning (which is why we have the weird loop target)
        for dst in self.data[1:] + self.data[:1]:
            distance += Chromosome.distances[(src, dst)]
            src = dst
        return distance

def main():
    c1 = Chromosome(4, False)
    Chromosome.distances = {(0,0):None, (0,1):1, (0,2):2, (0,3):3, (1,0):4, (1,1):None, (1,2):5, (1,3):6, (2,0):7, (2,1):8, (2,2):None, (2,3):9, (3,0):10, (3,1):11, (3,2):12, (3,3):None}
    print(c1.get_fitness())

if __name__ == '__main__':
    main()