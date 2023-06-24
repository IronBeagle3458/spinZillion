from Spin_model import Spin_Model

import matplotlib as plt

import random
import copy

POPULATION_SIZE = 10
MUTATION_RATE = 0

class Genetic_Stuff:
    def __init__(self, pop_size, mutation_rate) -> None:
        #Preset Variables
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate

        #These three should always be the same length because each Puzzle and Fitness value should match with a Solver
        self.population = []
        self.puzzles = []
        self.fitness = []

        self.prime_puzzle = self.puzzle_gen()

        #Traker of generations, for graphing
        self.gen_cnt = 0

        for i in range(pop_size):
            solver = self.solver_gen(50)
            self.population.append(solver)
            self.puzzles.append(copy.deepcopy(self.prime_puzzle))

    def puzzle_gen(self):
        puzzle = Spin_Model()
        puzzle.set_row(0, [0,5,3,1,5])
        puzzle.set_row(1, [0,4,4,2])
        puzzle.set_row(2, [3,2,2,1,4])
        puzzle.set_row(3, [1,5,3,3,4])
        puzzle.set_row(4, [0,5,1,2])
        return puzzle

    def solver_gen(self, move_cnt):
        solver = []
        for p in range(move_cnt):
            if p > 0:
                if solver[p-1] == 0:
                    solver.append(random.randint(1, 4))
                elif solver[p-1] == 1:
                    num = random.randint(0, 3)
                    if num >= 2:
                        num += 1
                    solver.append(num)
                elif solver[p-1] == 2:
                    num = random.randint(0, 3)
                    if num >= 1:
                        num += 1
                    solver.append(num)
                elif solver[p-1] == 3:
                    num = random.randint(0, 3)
                    solver.append(num)
                elif solver[p-1] == 4:
                    num = random.randint(0, 3)
                    if num == 3:
                        num += 1
                    solver.append(num)
            else:
                solver.append(random.randint(0, 4))
        return solver

    def interpreter(self, puzzle, move):
        if move == 0:
            puzzle.shift()
        elif move == 1:
            puzzle.move(0, 0)
        elif move == 2:
            puzzle.move(0, 1)
        elif move == 3:
            puzzle.move(2, 0)
        elif move == 4:
            puzzle.move(2, 1)

    def run(self):
        for i in range(self.pop_size):
            for move in self.population[i]:
                self.interpreter(self.puzzles[i], move)

    def score_fitness(self):
        for i in range(self.pop_size):
            #How well the solver did
            fitness = 0
            #tracks what step of the basic algorithm is used
            algor_cnt = 0
            for move in self.population[i]:
                if algor_cnt == 0 and move == 0:
                    algor_cnt += 1
                elif algor_cnt == 1 and move == 1:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 2 and move == 0:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 3 and move == 2:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 4 and move == 0:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 5 and move == 3:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 6 and move == 0:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 7 and move == 1:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 8 and move == 0:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 9 and move == 2:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 10 and move == 4:
                    algor_cnt += 1
                    fitness += 1
                elif algor_cnt == 11 and move == 0:
                    algor_cnt = 0
                    fitness += 1
                else:
                    algor_cnt = 0
            if self.puzzles[i].win_check():
                fitness += 100
            self.fitness.append(fitness)
