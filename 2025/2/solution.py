
class Solution():
    def get_nearest_invalid_repeated(self, num_str):
        if len(num_str) % 2 == 1:
            return '1' + '0' * (len(num_str) // 2)
        else:
            return num_str[:len(num_str)//2]

    def solve_a(self, input):
        answer = 0
        ranges = [x.strip() for x in input.split(',')]
        for id_range in ranges:
            first_str,second_str = id_range.split('-')
            low_invalid_repeated_str = self.get_nearest_invalid_repeated(first_str)
            high_invalid_repeated_str = self.get_nearest_invalid_repeated(second_str)
            first = int(first_str)
            second = int(second_str)
            low_invalid = int(low_invalid_repeated_str * 2)
            high_invalid = int(high_invalid_repeated_str * 2)
            if low_invalid < first:
                low_invalid_repeated_str = str(int(low_invalid_repeated_str) + 1)
            if high_invalid <= second:
                high_invalid_repeated_str = str(int(high_invalid_repeated_str) + 1)
            for num in range(int(low_invalid_repeated_str), int(high_invalid_repeated_str)):
                answer += int(str(num) * 2)
        return str(answer)

    def solve_b(self, input):
        answer = 0
        ranges = [x.strip() for x in input.split(',')]

        # split up ranges so each range starts and ends on numbers with the same number of digits
        id_ranges = []
        for id_range in ranges:
            first_str,second_str = id_range.split('-')
            if len(first_str) != len(second_str):
                id_ranges.append((first_str, '9'*len(first_str)))
                id_ranges.append(('1'+'0'*(len(second_str)-1), second_str))
            else:
                id_ranges.append((first_str, second_str))
        
        for id_range in id_ranges:
            num_digits = len(id_range[0])
            invalid_ids = set()

            # for each possible length of repeating numbers, find all invalid ids in that range
            possible_repeating_lengths = [x for x in range(1, num_digits) if num_digits % x == 0]
            for length in possible_repeating_lengths:
                times_repeating = num_digits // length
                first_repeating_str = id_range[0][:length]
                if int(first_repeating_str*times_repeating) < int(id_range[0]):
                    first_repeating_str = str(int(first_repeating_str) + 1)
                if int(first_repeating_str*times_repeating) > int(id_range[1]):
                    # no possible invalid ids with this length
                    continue
                second_repeating_str = id_range[1][:length]
                if int(second_repeating_str*times_repeating) <= int(id_range[1]):
                    second_repeating_str = str(int(second_repeating_str) + 1)
                for num in range(int(first_repeating_str), int(second_repeating_str)):
                    invalid_ids.add(int(str(num)*times_repeating))
            answer += sum(invalid_ids)

        return str(answer)
