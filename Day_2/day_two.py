with open("directions.txt") as f:
    lines = f.readlines()
    depth = 0
    horizontal_position = 0
    aim = 0
    #Part 1
    """
    for line in lines:
        direction, steps = line.split()
        if direction == "forward":
            horizontal_position += int(steps)
        elif direction == "up":
            depth -= int(steps)
        elif direction == "down":
            depth += int(steps)
    answer = depth * horizontal_position
    """
    #Part 2
    for line in lines:
        direction, num_of_steps = line.split()
        steps = int(num_of_steps)
        if direction == "forward":
            horizontal_position += steps
            depth += aim * steps
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps
    answer = depth * horizontal_position
print()
