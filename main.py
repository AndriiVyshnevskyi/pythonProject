import sys

# Отримання аргументів командного рядка
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Формування куплету
couplet = "la-" * x
couplet = couplet.rstrip("-")  # Видалення останнього дефісу

# Формування тексту пісеньки з куплетів
song = "Everybody sing a song: " + (couplet + " ") * y
song = song.rstrip()  # Видалення останнього пробілу

# Додавання крапки або окличного знака в кінці рядка
if z == 1:
    song += "!"
else:
    song += "."

# Виведення результату
print(song)
