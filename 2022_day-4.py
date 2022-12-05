my_file = open("input_2022_d4.txt", "r")
content = my_file.read()
puzzle_input_d4 = content.strip().split("\n")
my_file.close()

make_lists = [re.split(",|-",item) for item in puzzle_input_d4]
group_elves = [[int(item) for item in elf_group] for elf_group in make_lists]

def check_for_overlap(elf_group):
    elf_1,elf_2 = elf_group[0:2],elf_group[2:]
    
    elf_1_assigment = np.arange(elf_1[0],elf_1[1]+1)
    elf_2_assigment = np.arange(elf_2[0],elf_2[1]+1)
    
    if all(np.isin(elf_1_assigment,elf_2_assigment)):
        return True
    elif all(np.isin(elf_2_assigment,elf_1_assigment)):
        return True
    else:
        return False

def check_for_any_overlap(elf_group):
    elf_1,elf_2 = elf_group[0:2],elf_group[2:]
    
    elf_1_assigment = np.arange(elf_1[0],elf_1[1]+1)
    elf_2_assigment = np.arange(elf_2[0],elf_2[1]+1)
    
    if any(np.isin(elf_1_assigment,elf_2_assigment)):
        return True
    else:
        return False
    
#pt 1 ans
sum([check_for_overlap(elf_group) for elf_group in group_elves])
#pt 2 ans
sum([check_for_any_overlap(elf_group) for elf_group in group_elves])
