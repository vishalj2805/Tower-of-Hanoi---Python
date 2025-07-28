


def console_presentation(positions: dict[str, list[str]]):
    disks = {"disk_1":"#1#",
             "disk_2":"##2#",
             "disk_3":"##3##",
             "disk_4":"###4##",
             "disk_5":"###5###",
             "disk_6":"####6###",
             "disk_7":"####7####",
             "disk_8":"#####8####",
             "disk_9":"#####9#####"}

    towers = list(positions.keys())
    print(len(disks.get(positions.get(towers[0])[0])))
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



def hanoi_game(number_of_disks):
    pass



# disks = input("Enter Number of disks: ")

positioning = {"tower_1":["disk_6", "disk_7", "disk_5", "disk_2", "disk_1"],
               "tower_2":["disk_3"],
               "tower_3":["disk_4", "disk_8", "disk_9"]
               }

console_presentation(positioning)