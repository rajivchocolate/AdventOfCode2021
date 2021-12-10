with open("depth_measurements.txt") as f:
    lines = f.readlines()
    nums = [int(line.strip()) for line in lines]
    depth_increase = 0
    # Part 1
    # O(n)
    """
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            depth_increase += 1
    """
    #Part 2
    for i in range(0, len(nums)):
        initial_window_sum = nums[i] + nums[i+1] + nums[i+2]
        next_window_sum = nums[i+1] + nums[i+2] + nums[i+3]
        if initial_window_sum < next_window_sum:
            depth_increase += 1
print(depth_increase)