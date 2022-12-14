import sys
import time
import traceback
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from importlib import reload
from aocd import submit, get_data
import advent

class Start():
  def check_solution(self, event=None):
    file = open('test-input.txt')
    self.test_data = [line.rstrip().replace('\\n', '\n') for line in file.readlines()]

    try:
      reload(advent)
      solution = advent.Solution()
      successes = 0
      failures = 0
      for i in range(0, len(self.test_data), 2):
        expected = self.test_data[i+1]
        actual = str(solution.run(self.test_data[i]))
        if actual == expected:
          print('\033[92mCorrect answer: {}'.format(expected))
          successes += 1
        else:
          print('\033[91mExpected: {}, Actual: {}'.format(expected, actual))
          failures += 1
      if successes and not failures:
        solution = solution.run(self.data)
        print('Submitting Solution:', solution)
        submit(solution)
    except Exception as e:
      print(traceback.format_exc())

  def run(self):
    self.data = get_data()
    self.check_solution()

    event_handler = PatternMatchingEventHandler(patterns=['advent.py','test-input.txt'])
    event_handler.on_modified = self.check_solution
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
  Start().run()
