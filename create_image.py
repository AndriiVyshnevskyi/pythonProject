from PIL import Image, ImageDraw

# Встановіть розмір зображення
width, height = 100, 100

# Створити нове зображення з білим фоном
img = Image.new('RGB', (width, height), color = 'white')

# Можемо додати простий текст на зображення
draw = ImageDraw.Draw(img)
draw.text((10,10), "Hello", fill='black')

# Зберігаємо зображення
img.save('1.png')
