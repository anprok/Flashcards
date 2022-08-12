from collections import namedtuple

student_template = namedtuple('Student', ['name', 'age', 'department'])
alina = student_template('Alina', '22', 'linguistics')
alex = student_template('Alex', '25', 'programming')
kate = student_template('Kate', '19', 'art')
print(alina)
print(alex)
print(kate)