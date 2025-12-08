def ft_garden_summary(saved=0, day=0):
    if saved == 0:
        saved = int(input("Days until harvest: "))
        ft_count_harvest_recursive(saved, day+1)
    if day == saved:
        print("Day", day)
        print("Harvest time!")
        return 0
    if day > 0 :
        print("Day", day)
        ft_count_harvest_recursive(saved, day+1)
        
