def open_file(file):
    with open(file) as f:
        data = f.read()
    return data 

def make_grid(stones: str):
    grid = []
    platform = []
    for i in range(len(stones)):
        if stones[i] == '\n':
            grid.append(platform)
            platform = []
        else:
            platform.append(stones[i])
    grid.append(platform)
    return grid

def shift_north(grid: list[list]):
    for platform in range(len(grid)):
        for stones in range(len(grid[platform])):
            if grid[platform][stones] == 'O':
                shift = 1
                while grid[platform-shift][stones] != '#' and grid[platform-shift][stones] != 'O' and platform-shift>=0:
                    grid[platform-shift][stones] = 'O'
                    grid[platform-shift+1][stones] = '.'
                    shift+=1
    return grid

def shift_south(grid: list[list]):
    for platform in range(len(grid)-1,-1,-1):
        for stones in range(len(grid[platform])):
            if grid[platform][stones] == 'O':
                shift = 1
                while platform+shift<len(grid) and grid[platform+shift][stones] != '#' and grid[platform+shift][stones] != 'O':
                    grid[platform+shift][stones] = 'O'
                    grid[platform+shift-1][stones] = '.'
                    shift+=1
    return grid

def shift_west(grid: list[list]):
    for platform in range(len(grid)):
        for stones in range(len(grid[platform])):
            if grid[platform][stones] == 'O':
                shift = 1
                while grid[platform][stones-shift] != '#' and grid[platform][stones-shift] != 'O' and stones-shift>=0:
                    grid[platform][stones-shift] = 'O'
                    grid[platform][stones-shift+1] = '.'
                    shift+=1
    return grid

def shift_east(grid: list[list]):
    for platform in range(len(grid)):
        for stones in range(len(grid[platform])-1,-1,-1):
            if grid[platform][stones] == 'O':
                shift = 1
                while stones+shift<len(grid[platform]) and grid[platform][stones+shift] != '#' and grid[platform][stones+shift] != 'O':
                    grid[platform][stones+shift] = 'O'
                    grid[platform][stones+shift-1] = '.'
                    shift+=1
    return grid



def total_load(grid: list[list]):
    total_load = 0
    height = len(grid)
    for platform in range(len(grid)):
        for stones in range(len(grid[platform])):
            if grid[platform][stones] == 'O':     
                total_load = total_load + (height-platform)
    return total_load

def cycle(grid: list[list], number_cycles: int):
    for i in range(number_cycles):
        grid = shift_north(grid)
        grid = shift_west(grid)
        grid = shift_south(grid)
        grid = shift_east(grid)
    return grid


if __name__ == "__main__":
    stones = open_file("./day14input.txt")
    grid = make_grid(stones)
    grid = cycle(grid,1000000000)
    total_load(grid)
    print(total_load(grid))
    
