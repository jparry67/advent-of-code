import argparse
import importlib
import os
import sys
import time
from aocd import get_data, get_puzzle
from datetime import datetime
from pytz import timezone
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler

BASE_PYTHON_SOLUTION = '''
class Solution():
    def solve_a(self, input):
        answer = 0
        return str(answer)

    def solve_b(self, input):
        answer = 0
        return str(answer)
'''

def get_puzzle_day():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", dest="year", help="Advent Year")
    parser.add_argument("-d", "--day", dest="day", help="Puzzle Day")
    args = parser.parse_args()

    todayYear = datetime.now().year
    todayDay = datetime.now(timezone('US/Eastern')).day

    year = int(args.year) if args.year is not None else todayYear
    day = int(args.day) if args.day is not None else todayDay

    return year,day

class SolvePuzzle():
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.puzzle = get_puzzle(day=day, year=year)
        print(f'Puzzle URL: {self.puzzle.url}')
        self.solution_directory = self.init_solution_directory()
        self.init_solution_file()
        sys.path.append(self.solution_directory)
        self.solution_module = importlib.import_module('solution')
        self.save_puzzle_inputs()

    def init_solution_directory(self):
        solution_directory = f"{self.year}/{self.day}"
        if not os.path.exists(solution_directory):
            os.makedirs(solution_directory)
        return solution_directory

    def init_solution_file(self):
        try:
            f = open(f'{self.solution_directory}/solution.py', 'x')
            f.write(BASE_PYTHON_SOLUTION)
            f.close()
        except:
            pass

    def save_puzzle_inputs(self):
        try:
            input_file_name = f'{self.solution_directory}/input.txt'
            input_file = open(input_file_name, 'w')
            input_file.write(self.puzzle.input_data)
            input_file.close()
        except:
            pass
        for i,example in enumerate(self.puzzle.examples):
            try:
                example_input_file_name = f'{self.solution_directory}/test_input_{i+1}.txt'
                example_input_file = open(example_input_file_name, 'w')
                example_input_file.write(example.input_data)
                example_input_file.close()
            except:
                pass

    def check_puzzle_part(self, answer_prop, solver, answered):
        successes = 0
        failures = 0
        for i,example in enumerate(self.puzzle.examples):
            expected = getattr(example, answer_prop)
            actual = solver(example.input_data)
            if actual == expected:
                print(f'\033[92mCorrect answer: {expected}\033[0m')
                successes += 1
            else:
                print(f'\033[91mExpected: {expected}, Actual: {actual}\033[0m')
                failures += 1
        if successes and not failures:
            print('\033[34mTesting solution on real puzzle input...\033[0m')
            if answered:
                expected = getattr(self.puzzle, answer_prop)
                actual = solver(self.puzzle.input_data)
                if actual == expected:
                    print(f'\033[92mCorrect answer: {expected}\033[0m')
                else:
                    print(f'\033[91mExpected: {expected}, Actual: {actual}\033[0m')
            else:
                return solver(self.puzzle.input_data)

    def check_puzzle_solution(self, event=None):
        self.solution_module = importlib.reload(self.solution_module)
        Solution = getattr(self.solution_module, 'Solution')
        solution = Solution()

        try:
            print('\n\033[1m\033[44mTesting part a...\033[0m')
            answer = self.check_puzzle_part('answer_a', solution.solve_a, self.puzzle.answered_a)
            if answer:
                self.puzzle.answer_a = answer
            if self.puzzle.answered_a:
                print('\n\033[1m\033[44mTesting part b...\033[0m')
                answer = self.check_puzzle_part('answer_b', solution.solve_b, self.puzzle.answered_b)
                if answer:
                    self.puzzle.answer_b = answer
        except Exception as e:
            print(f'\033[91mprogram failed to run: \033[0m{e}')

    def loop_check_puzzle_solution(self):
        self.check_puzzle_solution()

        event_handler = PatternMatchingEventHandler(patterns=[f'{self.solution_directory}/solution.py'])
        event_handler.on_modified = self.check_puzzle_solution
        observer = Observer()
        observer.schedule(event_handler, '.', recursive=True)
        observer.start() 
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()

if __name__ == '__main__':
    year,day = get_puzzle_day()
    solve_puzzle = SolvePuzzle(year, day)
    solve_puzzle.loop_check_puzzle_solution()