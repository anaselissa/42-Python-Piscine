def ft_count_harvest_recursive():
    limite = int(input("Days until harvest: ")) + 1

    def count(current):
        if (current >= limite):
            return
        print(f"Day {current}")
        count(current + 1)
    count(1)
    print("Harvest time!")
