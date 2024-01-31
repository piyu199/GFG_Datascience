# Find Common Elements from the given multiple Lists.

def find_common_elements(lists):
    common_element={element:min(lst.count(element) for lst in lists) for element in set.intersection(*map(set, lists))}
    return common_element


list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 4, 4, 5]
list3 = [3, 4, 5, 5, 6]

result = find_common_elements([list1, list2, list3])

for element, frequency in result.items():
    print(f"Element: {element}, Frequency: {frequency}")