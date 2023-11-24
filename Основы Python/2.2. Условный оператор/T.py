lines = [input(), input(), input()]
bunny = 'зайка'

_lines = []
for line in lines:
    if bunny in line:
        _lines.append(line)
_lines.sort()

print(_lines[0], len(_lines[0]))