import random

pop = []
n = 8

class struct():
    def __init__(self):
        self.gene = []
        self.fitness = 0

    #def setGene(self, value):
    #    self.gene.append(value)

    #def getGene(self):
    #    return self.gene
    
    def getinfo(self):
        return self.gene, self.fitness

for i in range(10):
    pop.append(struct())
    for j in range(n):
        chromo = random.randint(0,1)
        pop[i].gene.append(chromo)

        if chromo == 1:
            pop[i].fitness += 1
            
   # print(pop[i].gene, pop[i].fitness)
    print(pop[i].getinfo())

#for i in pop:
    #print(i.gene, i.fitness)
