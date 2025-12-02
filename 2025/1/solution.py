
class Solution():
    def solve_a(self, input):
        answer = 0
        current = 50
        for code in input.split('\n'):
            direction = code[0]
            distance = int(code[1:])
            if direction == 'L':
                current -= distance
            else:
                current += distance
            while current < 0:
                current += 100
            while current >= 100:
                current -= 100
            if current == 0:
                answer += 1
        return str(answer)

    def solve_b(self, input):
        answer = 0
        current = 50
        for code in input.split('\n'):
            direction = code[0]
            distance = int(code[1:])
            if direction == 'L':
                new = current - distance
            else:
                new = current + distance
            while new >= 100:
                answer += 1
                new -= 100
            while new < 0:
                if current > 0 or new <= -100:
                    answer += 1
                new += 100
            if direction == 'L' and new == 0:
                answer += 1
            current = new
        return str(answer)
