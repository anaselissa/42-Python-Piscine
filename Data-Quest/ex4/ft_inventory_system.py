import sys


def main() -> None:
    if len(sys.argv) != 1:
        print("=== Inventory System Analysis ===")
        dic = {}
        tot_qty = 0
        for i in sys.argv[1:]:
            try:
                parts = i.split(':')
                if len(parts) != 2:
                    raise IndexError
                if parts[0] not in dic:
                    dic[parts[0]] = int(parts[1])
                    tot_qty += dic[parts[0]]
                else:
                    print(f"Redundant item {parts[0]} - discarding")
            except IndexError:
                print("Error - invalid parameter: ", i)
            except ValueError as e:
                print(f"Quantity error for ’{parts[0]}’:", e)
        if tot_qty == 0:
            print("please enter at least one correct argument")
            return
        print("Got inventory: ", dic)
        items = list(dic.keys())
        most_abundant = items[0]
        least_abundant = items[0]

        for key in items:
            if dic[key] > dic[most_abundant]:
                most_abundant = key
            if dic[key] < dic[least_abundant]:
                least_abundant = key

        print("Item list: ", list(dic.keys()))
        print(f"Total quantity of the {len(dic)} items: ", tot_qty)
        for key in dic:
            print(f"Item {key} represents "
                  f"{round((dic[key]) * 100/tot_qty, 1)}%")
        print(f"Item most abundant: {most_abundant} with quantity "
              f"{dic[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity "
              f"{dic[least_abundant]}")
        dic.update({'magic_item': 1})
        print("Updated inventory: ", dic)


if __name__ == "__main__":
    main()
