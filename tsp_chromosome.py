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
    mutation_rate = .1

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
            Chromosome.__reproduce__(mother, father, start, end), start, end

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

import time

def main():
    Chromosome.mutation_rate = 0
    f = Chromosome(10, False)
    m = Chromosome(10, False)
    m.data.reverse()
    c1, c2, s, e = Chromosome.reproduce(f, m)
    print('start: {}\tend: {}'.format(s, e))
    print(c1.data)
    print(c2.data)

if __name__ == '__main__':
    main()