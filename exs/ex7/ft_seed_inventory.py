def ft_seed_inventory(seed_type, quantity, unit):
    seed_type_formatted = seed_type
    if unit == "packets":
        print(f"{seed_type_formatted} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type_formatted} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type_formatted} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit provided.")
