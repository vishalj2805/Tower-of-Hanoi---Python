import random

disks = {"disk_1":"#1#",
         "disk_2":"##2#",
         "disk_3":"##3##",
         "disk_4":"###4##",
         "disk_5":"###5###",
         "disk_6":"####6###",
         "disk_7":"####7####",
         "disk_8":"#####8####",
         "disk_9":"#####9#####"
         }


def console_presentation(positions: dict[str, list[str]]):

    towers = list(positions.keys())

    for row in range(9,0,-1):
        if len(positions.get(towers[0])) < row and len(positions.get(towers[1])) < row and len(positions.get(towers[2])) < row:
            print("")
        else:
            for tower in towers:
                if len(list(positions.get(tower))) == row:
                    print(disks.get(positions.get(tower)[row-1]), end="")
                    print(" " * (11 + (11 - len(disks.get(positions.get(tower)[row-1])))), end="")
                elif len(list(positions.get(tower))) > row:
                    print(disks.get(positions.get(tower)[row-1]), end="")
                    print(" " * (11 + (11 - len(disks.get(positions.get(tower)[row-1])))), end="")
                else:
                    print(" " * 22, end="")

            print("")


def starting_position(number_of_disks: int):
    towers = {"tower_1":[], "tower_2":[], "tower_3":[]}
    disks = [num for num in range(1, number_of_disks+1)]
    for i in range(1, number_of_disks+1):
        disk_no = random.choice(disks)
        tower_no = random.choice(["tower_1", "tower_2", "tower_3"])
        towers[tower_no].append(f"disk_{disk_no}")
        disks.remove(disk_no)

    return towers


steps_count = 0
def select_option(positioning: dict[str, list[str]]):
    print("\n")
    towers_upper_disk = {"tower_1_upper_disk": "No Disc" if (len(positioning["tower_1"]) == 0) else positioning["tower_1"][-1],
        "tower_2_upper_disk":"No Disc" if (len(positioning["tower_2"]) == 0) else positioning["tower_2"][-1],
        "tower_3_upper_disk":"No Disc" if (len(positioning["tower_3"]) == 0) else positioning["tower_3"][-1]
    }

    option = 1
    move_disk = []
    for tower_no in range(1,4):
        other_tower_no = [*range(1,4)]
        other_tower_no.remove(tower_no)

        if towers_upper_disk[f"tower_{tower_no}_upper_disk"] != "No Disc":
            for other_tower in other_tower_no:
                if towers_upper_disk[f"tower_{other_tower}_upper_disk"] == "No Disc":
                    action = f"Press {option}: Move {towers_upper_disk[f"tower_{tower_no}_upper_disk"]} in tower_{other_tower}"
                    print(action)
                    move_disk.append(action)
                    option += 1
                elif towers_upper_disk[f"tower_{tower_no}_upper_disk"].split("_")[-1] < towers_upper_disk[f"tower_{other_tower}_upper_disk"].split("_")[-1]:
                    action = f"Press {option}: Move {towers_upper_disk[f"tower_{tower_no}_upper_disk"]} above {towers_upper_disk[f"tower_{other_tower}_upper_disk"]}"
                    print(action)
                    move_disk.append(action)
                    option += 1

    option_selected = input("Select from above options: ")
    global steps_count
    steps_count += 1
    option_selected = [move for move in move_disk if f"Press {option_selected}" in move][0]
    print("Selected Option: " + option_selected)

    return make_move(option_selected, positioning)


def make_move(option_selected: str, positioning: dict[str, list[str]]):
    print("=" *100)
    source_disk, destination_disk = [word for word in option_selected.split(" ") if "disk_" in word or "tower_" in word]

    disk_to_move = ""
    to_tower = ""
    for key in positioning.keys():
        if not positioning.get(key) and key != destination_disk:
            continue

        if key == destination_disk or positioning.get(key)[-1] == destination_disk:
            to_tower = key
        elif not positioning.get(key) or positioning.get(key)[-1] == source_disk:
            disk_to_move = positioning.get(key).pop()

    positioning.get(to_tower).append(disk_to_move)

    return positioning

def game_won(position: dict[str, list[str]], number_of_disks):

    for key, value in position.items():
        disk_nos = [int(disk.split("_")[1]) for disk in value]

        if list(range(number_of_disks, 0, -1)) == disk_nos:
            return True

    return False



def hanoi_game(number_of_disks):
    global steps_count
    position = starting_position(number_of_disks)

    while True:
        console_presentation(position)
        position = select_option(position)
        if game_won(position, number_of_disks):
            break

    print(console_presentation(position))
    print(f"Completed Game in Steps: {steps_count}")


hanoi_game(3)

