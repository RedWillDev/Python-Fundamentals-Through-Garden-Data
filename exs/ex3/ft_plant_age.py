def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    match days:
        case d if d >= 60:
            print("Plant is ready to harvest!")
        case _:
            print("Plant needs more time to grow.")
