numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_1 = numbers[:4] + numbers[5:]
m = sum(numbers_1) / len(numbers)
numbers[4] = m
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
