file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]

highest = 0
allSeats = set()
for line in input:
    minimum_row = 0
    maximum_row = 127
    minimum_col = 0
    maximum_col = 7
    for letter in line:
        halfway_row = (maximum_row - minimum_row + 1) // 2 + minimum_row
        halfway_col = (maximum_col - minimum_col + 1) // 2 + minimum_col
        if letter == 'F':
            maximum_row = halfway_row - 1
        elif letter == 'B':
            minimum_row = halfway_row
        if letter == 'L':
            maximum_col = halfway_col - 1
        elif letter == 'R':
            minimum_col = halfway_col
    seatId = minimum_row * 8 + minimum_col
    allSeats.add(seatId)
    if seatId > highest:
        highest = seatId
    
print(highest)
print(allSeats)