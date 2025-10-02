from math import sqrt, pi
import random

# 1) Class for input/output of a stringъъ
class IOString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input().rstrip("\n")

    def printString(self):
        print(self.s.upper())

# 2) Shape and Square
class Shape:
    def area(self) -> float:
        return 0.0

class Square(Shape):
    def __init__(self, length: float):
        self.length = length

    def area(self) -> float:
        return self.length ** 2

# 3) Rectangle inherits from Shape
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

# 4) Point (обычный класс, без dataclass)
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# 5) Bank Account
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be > 0")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be > 0")
        if amount > self.balance:
            print("Not enough balance")
            return self.balance
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self.balance:.2f})"

# 6) Check primes
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime_list(nums):
    return list(filter(lambda x: is_prime(x), nums))

# 7) grams -> ounces
def grams_to_ounces(grams: float) -> float:
    return 28.3495231 * grams

# 8) Fahrenheit -> Celsius
def f_to_c(F: float) -> float:
    return (5.0 / 9.0) * (F - 32.0)

# 9) Chickens & Rabbits puzzle
def solve(numheads: int, numlegs: int):
    if numlegs % 2 != 0:
        return "No solution"
    halfL = numlegs // 2
    y = halfL - numheads
    x = numheads - y
    if x < 0 or y < 0 or 2*x + 4*y != numlegs:
        return "No solution"
    return {"chickens": x, "rabbits": y}

# 10) filter primes from input
def filter_prime(s: str):
    nums = list(map(int, s.split()))
    return filter_prime_list(nums)

# 11) Permutations of string (сами вручную)
def all_permutations(s: str):
    if len(s) <= 1:
        return [s]
    perms = []
    for i, ch in enumerate(s):
        for p in all_permutations(s[:i] + s[i+1:]):
            perms.append(ch + p)
    return perms

# 12) Reverse words
def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split()[::-1])

# 13) has_33
def has_33(nums) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 14) spy_game
def spy_game(nums) -> bool:
    target = [0, 0, 7]
    idx = 0
    for n in nums:
        if idx < 3 and n == target[idx]:
            idx += 1
    return idx == 3

# 15) Sphere volume
def sphere_volume(r: float) -> float:
    return (4.0 / 3.0) * pi * (r ** 3)

# 16) Unique elements
def unique_list(lst):
    seen = {}
    result = []
    for x in lst:
        if x not in seen:
            seen[x] = True
            result.append(x)
    return result

# 17) Palindrome check
def is_palindrome(s: str) -> bool:
    t = ''.join(ch.lower() for ch in s if ch.isalnum())
    return t == t[::-1]

# 18) Histogram
def histogram(lst):
    for n in lst:
        print('*' * n)

# 19) Guess the number game
def guess_number_game():
    name = input("Hello! What is your name?\n").strip() or "Player"
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret = random.randint(1, 20)
    tries = 0
    while True:
        print("Take a guess.")
        try:
            g = int(input().strip())
        except ValueError:
            print("Please enter an integer.")
            continue
        tries += 1
        if g < secret:
            print("\nYour guess is too low.")
        elif g > secret:
            print("\nYour guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {tries} guesses!")
            break

# 20) Movies dataset
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

def good_movie(movie):
    return movie.get("imdb", 0) > 5.5

def good_movies(ms):
    return [m for m in ms if good_movie(m)]

def by_category(ms, category: str):
    return [m for m in ms if m.get("category") == category]

def avg_imdb(ms):
    if not ms:
        return 0.0
    return sum(m.get("imdb", 0.0) for m in ms) / len(ms)

def avg_imdb_by_category(ms, category: str):
    subset = by_category(ms, category)
    return avg_imdb(subset)
