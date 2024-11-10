disk_size = 1.44
Mb_in_Kb = 1024
Kb_in_b = 1024
symbol_weight = 4
page = 100
line = 50
symbol = 25

book = symbol_weight * symbol * line * page
disk = disk_size * Mb_in_Kb * Kb_in_b
count = (disk // book)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", round(count))
