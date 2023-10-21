n = input()
segments = []
count = 0

for i in range(int(n)):
    coordinates = input().split()
    segments.append([
        int(coordinates[0]), 
        int(coordinates[1])
    ])

while len(segments) != 0:
    r_min = min([i[1] for i in segments])
    _segments = []
    for i in segments:
        if i[1] > r_min and i[0] > r_min:
            _segments.append(i)
    segments = _segments
    count += 1

print(count)

