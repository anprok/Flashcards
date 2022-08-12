def check(x):
    lower_border = 120
    upper_border = 137

    if lower_border < x < upper_border:
        print(x)
    else:
        print("That's a bad present!")