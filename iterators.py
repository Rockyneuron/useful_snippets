"""Recordatory snippets for map, filter, reduce, generators
and list comprehensions
"""

numbers=list(range(1,16))
print('numnbers {}'.format(numbers))
numbers_even=list(filter(lambda x: x%2==0,numbers));
print(f'filter even numbers{numbers_even}')
square_even=list(map(lambda x: x**2,numbers_even));
print(f'square numbers {square_even}')

# cooler

process_numbers=list(map(lambda x:x**2,filter(lambda x: x%2==0,numbers)))
print(f'one step processed numbers {process_numbers}')

# with a list comprehension

process_numbers=[num2**2 for num2 in ([num for num in numbers if num%2==0])]
print('Same with list comprehension {}'.format(process_numbers))


# Infinite nested comprehension loop

process_inf=[num**2 for num in 
    [num**2 for num in
    [num**2 for num in 
    ([num for num in numbers if num%2==0])]]]
print('Inf comprehension {}'.format(process_inf))

# Same with a generator to save memory

process_inf_generator=(num**2 for num in 
    (num**2 for num in
    (num**2 for num in 
    ((num for num in numbers if num%2==0)))))

print('Inf generator {}'.format(list(process_inf_generator)))

#Zip to unpack and relate lists and tuples. Smaller iterable determines the end of pairing

names = ['Bob', 'Sue', 'Amanda']
surnames=['Cloak','Morgan','Knoles']
grade_point_averages = (3.5, 4.0, 3.75) 

for name, gpa,surname in zip(names, grade_point_averages,surnames):
    print(f'Name={name}; GPA={gpa}; surname={surname}')