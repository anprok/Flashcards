info = input().split(', ')
name, age, city, *miscellaneous = info
print("name: {}".format(name))
print("age: {}".format(age))
print("city: {}".format(city))
print("miscellaneous:", *miscellaneous)