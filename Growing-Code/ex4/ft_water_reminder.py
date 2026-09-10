def ft_water_reminder():
    num_day = int(input("Days since last watering: "))
    if (num_day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
