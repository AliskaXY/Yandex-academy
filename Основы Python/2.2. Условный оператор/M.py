elf = int(input())
dwarf = int(input())
human = int(input())

if elf // 10 == dwarf // 10 and elf // 10 == human // 10:
    print(elf // 10)
else:
    print(elf % 10)