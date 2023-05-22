
def Number_boundaries():
    value = float(input("Enter an arbitrary value: "))
    wall = float(input("Enter the boundary value: "))

    if value < wall:
        print(f"{value} less than the boundary value {wall}")
    elif value > wall:
        print(f"{value} greater than the boundary value {wall}")
        if value > wall * 3:
            print(f"{value} more than the boundary value by 3 times {wall}")
    else:
        print(f"{value} equal to the boundary value {wall}")
    
if __name__ == '__main__':
    Number_boundaries()


