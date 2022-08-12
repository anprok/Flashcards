def check_integer(num):
    lower_bound, upper_bound = 45, 67
    if lower_bound <= num <= upper_bound:
        return num
    raise NotInBoundsError()

def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as err:
        print(err)
    else:
        print(num)