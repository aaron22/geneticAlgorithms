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
    mutationRate = .1

    def __init__(self, size=128):
        self.size=size
        self._random()

    def _random(self):
        self.data = [random.choice([0,1]) for i in range(self.size)]

    def reproduce(father, mother):
        child1 = Chromosome(father.size)
        child2 = Chromosome(father.size)
        pivot = random.randrange(father.size)
        child1.data = father.data[:pivot] + mother.data[pivot:]
        child2.data = mother.data[:pivot] + father.data[pivot:]
        return (child1, child2, pivot)

    def _mutate(self):
        if random.random() < Chromosome.mutationRate:
            bitToFlip = random.randrange(self.size)
            self.data[bitToFlip] = 0 if self.data[bitToFlip] == 1 else 1
            return "yes"
        return "no"

    def get_fitness(self):
        return sum(self.data)

def main():
    #print("don't run this file by itself!")

if __name__ == '__main__':
    main()