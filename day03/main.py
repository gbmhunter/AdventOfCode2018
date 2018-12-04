# PART 1

with open('input.txt', 'r') as file:
    claims = []
    for line in file:
        claims.append(line.strip())

grid = []
for i in range(1000):
    grid.append([0]*1000)

overlapping_claims = {}
for claim in claims:    
    left_edge = int(claim[claim.find('@') + 2:claim.find(',')])
    top_edge = int(claim[claim.find(',') + 1: claim.find(':')])

    width = int(claim[claim.find(':') + 1: claim.find('x')])
    height = int(claim[claim.find('x') + 1:])

    for i in range(left_edge, left_edge + width):
        for j in range(top_edge, top_edge + height):
            grid[i][j] += 1

count = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            count += 1

print(f'count = {count}')

# PART 2

overlapping_claims = {}
for claim in claims:
    left_edge = int(claim[claim.find('@') + 2:claim.find(',')])
    top_edge = int(claim[claim.find(',') + 1: claim.find(':')])

    width = int(claim[claim.find(':') + 1: claim.find('x')])
    height = int(claim[claim.find('x') + 1:])

    overlapping_claims[claim] = False
    for i in range(left_edge, left_edge + width):
        for j in range(top_edge, top_edge + height):
            if grid[i][j] > 1:
                overlapping_claims[claim] = True

for claim in claims:
    if not overlapping_claims[claim]:
        print(f'Non-overlapping claim = {claim}')