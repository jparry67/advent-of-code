from utils import Fns

class Solution():
  def add_answer(self, answer, x, cycle):
    if cycle % 40 == 20:
      return answer + x * cycle
    return answer

  def draw_pixel(self, x, cycle):
    x_pos = (cycle-1) % 40
    if (x_pos == x-1 or x_pos == x or x_pos == x+1):
      print('#', end = "")
    else:
      print('.', end = "")
    if x_pos == 39:
      print()

  def run(self, input):
    answer = 0
    curr_cycle = 1
    x = 1
    self.draw_pixel(x, curr_cycle)
    for line in input.split('\n'):
      line = line.strip()
      if line == 'noop':
        curr_cycle += 1
        answer = self.add_answer(answer, x, curr_cycle)
        self.draw_pixel(x, curr_cycle)
      elif line[:4] == 'addx':
        curr_cycle += 1
        answer = self.add_answer(answer, x, curr_cycle)
        self.draw_pixel(x, curr_cycle)
        curr_cycle += 1
        com, num = line.split()
        x += int(num)
        answer = self.add_answer(answer, x, curr_cycle)
        self.draw_pixel(x, curr_cycle)
    return answer