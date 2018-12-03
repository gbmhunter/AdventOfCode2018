# PART 1

with open('input.txt', 'r') as file:
    claims = []
    for line in file:
        claims.append(line.strip())

grid = []
for i in range(1000):
    grid.append([0]*1000)

for claim in claims:    
    left_edge = int(claim[claim.find('@') + 2:claim.find(',')])
    top_edge = int(claim[claim.find(',') + 1: claim.find(':')])

    width = int(claim[claim.find(':') + 1: claim.find('x')])
    height = int(claim[claim.find('x') + 1:])
    print(f'left_edge = {left_edge}, top_edge = {top_edge}, width = {width}, height = {height}')

    for i in range(left_edge, left_edge + width):
        for j in range(top_edge, top_edge + height):
            grid[i][j] += 1

count = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            count += 1

print(f'count = {count}')