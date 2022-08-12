def check(x):
    if x.isdigit():
        lower_border = 202
        if int(x) >= lower_border:
            print(x)
        else:
            print("There are less than 202 apples! You cheated me!")
    else:
        print("It is not a number!")
