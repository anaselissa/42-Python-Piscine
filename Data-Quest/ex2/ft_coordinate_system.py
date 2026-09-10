import math


def get_player_pos() -> tuple[float, float, float]:
    print("Get a first set of coordinates")

    while (True):
        coords_list = []
        coordinates = input("Enter new coordinates as floats in"
                            "format ’x,y,z’: ").split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        try:
            for coord_val in coordinates:
                coords_list += [(float(coord_val))]
            return (coords_list[0], coords_list[1], coords_list[2])
        except ValueError:
            print(f"Error on parameter ’{coord_val}’: "
                  f"could not convert string to float: {coord_val}")


def main() -> None:
    print("=== Game Coordinate System ===")

    coordinates = get_player_pos()
    x1, y1, z1 = coordinates

    print("Got a first tuple: ", coordinates)
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist_to_origin = (x1*x1 + y1*y1 + z1*z1)
    print("Distance to center: ", round(math.sqrt(dist_to_origin), 4))
    print("Get a second set of coordinates")
    while (True):
        coords_list2 = []
        new_coordinates = input("Enter new coordinates as floats in"
                                "format ’x,y,z’: ").split(",")
        if (len(new_coordinates) == 3):
            try:
                for coord_val in new_coordinates:
                    coords_list2 += [(float(coord_val))]
                break
            except ValueError as e:
                print(f"Error on parameter ’{coord_val}’:", e)
        else:
            print("please enter exactly 3 number")
    x2 = coords_list2[0]
    y2 = coords_list2[1]
    z2 = coords_list2[2]

    ns = round(math.sqrt((x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)

    print("Distance between the 2 sets of coordinates: ", ns)


if __name__ == "__main__":
    main()
