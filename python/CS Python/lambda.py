nums = [5, 12, 7, 20, 3, 15]
people = [('Alice', 17), ('Bob', 21), ('Charlie', 19)]

print(sorted(list(item for item in nums if item >= 10) + list(item * 2 for item in nums if item < 10)))
print(sorted(list(person for person in people if person[1] >= 18)))