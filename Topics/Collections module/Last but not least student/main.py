# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
marks = OrderedDict(json.loads(input()))

marks['Max'] = 100
marks.move_to_end('Max', last=False)
print(marks)