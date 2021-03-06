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

import random

class Chromosome(object):
    '''represents a solution for a maximum-sum binary array problem'''
    mutation_rate = .1

    def __init__(self, size=128):
        '''loads the chromosome with random data of the specified size'''
        self.size=size
        self._random()

    def _random(self):
        '''loads the chromosome with random data'''
        self.data = [random.choice([0,1]) for i in range(self.size)]

    def reproduce(father, mother):
        '''
        creates two offspring from the specified parents.
        a three-tuple is returned, consisting of:
            [0] = the first child, generated by the first segment of the father
                  and the second segment of the mother
            [1] = the second child, generated by the first segment of the mother
                  and the second segment of the father
            [2] = the pivot index used to split the mother and father into
                  segments
        '''
        child1 = Chromosome(father.size)
        child2 = Chromosome(father.size)
        pivot = random.randrange(father.size)
        child1.data = father.data[:pivot] + mother.data[pivot:]
        child1._mutate()
        child2.data = mother.data[:pivot] + father.data[pivot:]
        child2._mutate()
        return (child1, child2, pivot)

    def _mutate(self):
        '''
        Randomly determines whether a mutation should occur and, if so, flips a
        randomly selected bit in the chromosome; return value indicates whether
        a mutation occurred.
        '''
        if random.random() < Chromosome.mutation_rate:
            bitToFlip = random.randrange(self.size)
            self.data[bitToFlip] = 0 if self.data[bitToFlip] == 1 else 1
            return True
        return False

    def get_fitness(self):
        '''returns the fitness value of the chromosome'''
        return sum(self.data)

def main():
    # running this file by itself shouldn't do anything
    pass

if __name__ == '__main__':
    main()