# demo_import.py
from Lab31PP2 import (
    # функции
    is_prime, reverse_words, sphere_volume, good_movies, movies,
    grams_to_ounces, f_to_c, solve, all_permutations, spy_game,
    # классы
    Account, Point, Square, Rectangle
)

# --- ФУНКЦИИ ---
print("Проверка простого числа 29:", is_prime(29))
print("Переворот слов:", reverse_words("Привет мир из KBTU"))
print("Объем сферы радиусом 5:", sphere_volume(5))

print("100 грамм в унциях:", grams_to_ounces(100))
print("212°F в °C:", f_to_c(212))
print("Задача про кур и кроликов (35 голов, 94 ноги):", solve(35, 94))
print("Перестановки строки 'abc':", all_permutations("abc"))
print("Spy game для [1,2,4,0,0,7,5]:", spy_game([1,2,4,0,0,7,5]))

print("\nФильмы с рейтингом > 5.5:")
for m in good_movies(movies):
    print("-", m["name"], m["imdb"])

# --- КЛАССЫ ---
print("\n=== Классы ===")

# Account
acc = Account("KBTU Student", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # проверка превышения
print("Счёт после операций:", acc)

# Point
p1 = Point(0, 0)
p2 = Point(3, 4)
print("Расстояние между точками:", p1.dist(p2))
p1.move(1, 2)
print("После сдвига p1:", end=" ")
p1.show()

# Square / Rectangle
sq = Square(5)
rect = Rectangle(3, 7)
print("Площадь квадрата (5):", sq.area())
print("Площадь прямоугольника (3x7):", rect.area())
