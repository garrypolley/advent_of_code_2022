def read_input():
    with open("./input.txt") as f:
        return f.read().splitlines()


def group_by_elf(data):
    elf_info = {}
    elf_num = 0
    for line in data:
        if elf_num not in elf_info:
            elf_info[elf_num] = {
                "food": [],
            }

        if line == "":
            elf_num += 1
            continue

        elf_info[elf_num]["food"].append(int(line))

    for values in elf_info.values():
        values["sum"] = sum(values["food"])

    largest_sum = 0
    largest_elf = elf_info[0]
    for elf, values in elf_info.items():
        if values["sum"] > largest_sum:
            largest_sum = values["sum"]
            largest_elf = elf_info[elf]

    return elf_info, largest_elf

def order_elves_by_most_calories(elf_info):
    return sorted(elf_info.items(), key=lambda x: x[1]["sum"], reverse=True)

all_elves, largest_elf = group_by_elf(read_input())
