"""
genetic.py

Contains class definition for Genetic Algorithm
"""

from copy import deepcopy
from random import randint

from puzzle import Puzzle

class Genetic(Puzzle):

    """
    Genetic
    """

    def __init__(self):

        """
        Initializes class through user input

        Performs basic input validation
        """

        super().__init__()

        self.n_generations = int(input("Enter number of generations: "))
        self.mutation_prob = float(input("Enter mutation probability: "))
        self.crossover_prob = float(input("Enter crossover probability: "))
        self.population_size = int(input("Enter size of population: "))
        self.depth = int(input("Enter maximum number of moves: "))

        assert self.mutation_prob > 0, f"Mutation Probability {self.mutation_prob} too low"
        assert self.mutation_prob < 1, f"Mutation Probability {self.mutation_prob} too high"
        assert self.crossover_prob > 0, f"Crossover Probability {self.crossover_prob} too low"
        assert self.crossover_prob < 1, f"Crossover Probability {self.crossover_prob} too high"

        self.population = self.generate_population()
        print(self.population)

    def generate_population(self):

        """
        Generates initial population based on hyperparameters
        """

        population = []

        digits = "LRUD"

        for _ in range(self.population_size):
            population.append("".join([digits[randint(0, 3)] for _ in range(self.depth)]))

        return population

    def mutate(self):

        """
        Mutates population based on hyperparameters
        """

        new_population = []

        n_itr = int(self.population_size * self.mutation_prob)
        for _ in range(n_itr):

            idx = randint(0, self.population_size - 1)
            old_pos = randint(0, self.depth - 1)
            new_pos = randint(0, self.depth - 1)

            individual = list(deepcopy(self.population[idx]))
            individual[old_pos], individual[new_pos] = individual[new_pos], individual[old_pos]
            individual = "".join(individual)

            new_population.append(individual)

        return self.evaluate(new_population)

    def crossover(self):

        """
        Performs crossover based on hyperparameters
        """

        new_population = []

        n_itr = int(self.population_size / 2)
        split = int(self.depth / 2)

        for itr in range(int(n_itr * self.crossover_prob)):
            new_population.append(self.population[itr][:split] + self.population[itr+n_itr][split:])
            new_population.append(self.population[itr+n_itr][:split] + self.population[itr][split:])

        return self.evaluate(new_population)

    def evaluate(self, new_population):

        """
        Evaluates new_population and self.population and
        updates self.population with population_size best individuals
        """

        switch_case = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        scores = []
        temp_population = deepcopy(self.population)
        temp_population += new_population
        self.population = []

        for itr, individual in enumerate(temp_population):
            score = 0
            initial_state = deepcopy(self.state)
            for move in individual:
                if self.shift(switch_case[move]):
                    score -= 1
                    self.state = self.states[-1]
                else:
                    distance = self.manhattan_distance(-1)
                    if distance == 0:
                        print(individual)
                        return True
                    scores.append([itr, score + distance])
                    self.state = initial_state
                    self.states = [self.state]
                    self.states_check = {self.flatten(self.state): True}
                    break

        scores.sort(key=lambda x: x[1])

        for itr in range(self.population_size):
            self.population.append(temp_population[scores[itr][0]])

        return False

    def solver(self):

        """
        Genetic solver
        """

        self.evaluate([])

        for _ in range(self.n_generations):
            if self.mutate():
                return
            if self.crossover():
                return


if __name__ == "__main__":
    genetic = Genetic()
    genetic.solver()
