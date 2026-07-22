# pygame_test.py

# Импортировать библиотеку Pygame
import pygame

# Инициализировать библиотеку Pygame
pygame.init()


# Создать окно размером 800×600 точек (или пикселей)
screen = pygame.display.set_mode((800, 600))
# Задать окну заголовок
pygame.display.set_caption('Пример графического окна Pygame')


running = True

# Описание главного цикла игры
# Этот цикл работает до тех пор, пока пользователь не закроет окно
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисование линии
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (700, 500), 5)

    # Рисование квадрата
    # Квадрат с верхним левым углом в точке (300, 200) и размерами 200×200 
    # будет нарисован зелёным цветом
    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(300, 200, 200, 200))

    # Отобразить нарисованные элементы в окне
    pygame.display.update()


# Деинициализирует все модули Pygame, которые были инициализированы ранее
pygame.quit()

from math import floor

def find_max_even_number(numbers):
    """
    Ищет максимальное чётное значение в списке положительных целых значений, переданном в параметр функции.
    """
    CurrentMax = 0
    for number in numbers:
        if number % 2 == 0: CurrentMax = max(number, CurrentMax)
    return CurrentMax

max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number() другие списки:
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f'Максимальное чётное число: {max_even}')
