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

def make_move(positioning: dict[str, list[str]]):
    print("\n")
    tower_1_upper_disk = "No Disc" if (len(positioning["tower_1"]) == 0) else positioning["tower_1"][-1]
    tower_2_upper_disk = "No Disc" if (len(positioning["tower_2"]) == 0) else positioning["tower_2"][-1]
    tower_3_upper_disk = "No Disc" if (len(positioning["tower_3"]) == 0) else positioning["tower_3"][-1]
    print(tower_1_upper_disk)
    print(tower_2_upper_disk)
    print(tower_3_upper_disk)

    for tower in range(1,4):


        option = 1
        if tower_1_upper_disk != "No Disc":
            if tower_2_upper_disk == "No Disc":
                print(f"Press {option}: Move {tower_1_upper_disk} in Tower 2")
                option += 1
            elif tower_1_upper_disk.split("_")[-1] < tower_2_upper_disk.split("_")[-1]:
                print(f"Press {option}: Move {tower_1_upper_disk} above {tower_2_upper_disk}")
                option += 1

            if tower_3_upper_disk != "No Disc":
                if tower_3_upper_disk == "No Disc":
                    print(f"Press {option}: Move {tower_1_upper_disk} in Tower 3")
                    option += 1
                elif tower_1_upper_disk.split("_")[-1] < tower_3_upper_disk.split("_")[-1]:
                    print(f"Press {option}: Move {tower_1_upper_disk} above {tower_3_upper_disk}")
                    option += 1










def hanoi_game(number_of_disks):
    position = starting_position(number_of_disks)
    console_presentation(position)
    make_move(position)



# disks = input("Enter Number of disks: ")

hanoi_game(9)

