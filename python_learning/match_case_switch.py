def day_of_week(day):
    match day:
        case 1:
            return "It's sunday"
        case 2:
            return "It's monday"
        case 3:
            return "It's tuesday"
        case 4:
            return "It's wednesday"
        case 5:
            return "It's thursday"
        case 6:
            return "It's friday"
        case 7: 
            return "It's saturday"
        case _:
            return "Not a valid number"

print(day_of_week(2))