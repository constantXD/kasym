import math
import time

numbers = [2, 3, 4, 5]
result = 1
for i in numbers:
    result *= i
print(result)

def count_case(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    return upper, lower

string = input("Enter a string: ")
upper, lower = count_case(string)
print(f"Upper case: {upper}, Lower case: {lower}")

def palindrome(s):
    return s == s[::-1]

string = "madam"
print(palindrome(string))

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

number = int(input())
delay = int(input())
result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

tup = (True, True, False, True, True, True, True)
print(all(tup))

import os
from colorama import Fore
import sys, tty, termios

def list_only(path):
    print(Fore.CYAN + "Directories:")
    names = os.listdir(path)
    for n in names:
        p = os.path.join(path, n)
        if os.path.isdir(p):
            print(n)

    print(Fore.GREEN + "\nFiles:")
    names = os.listdir(path)
    for n in names:
        p = os.path.join(path, n)
        if os.path.isfile(p):
            print(n)

    print(Fore.YELLOW + "\nAll:")
    names = os.listdir(path)
    for n in names:
        print(n)

def check_access(path):
    if os.path.exists(path):
        print(Fore.GREEN + "Exists: True")
        print("Readable:", os.access(path, os.R_OK))
        print("Writable:", os.access(path, os.W_OK))
        print("Executable:", os.access(path, os.X_OK))
    else:
        print(Fore.RED + "Exists: False")

def path_info(path):
    if os.path.exists(path):
        print(Fore.GREEN + "Path exists")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print(Fore.RED + "Path does not exist")

def count_lines(file_path):
    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    print(Fore.YELLOW + "Lines:", len(lines))

def write_list(file_path, items):
    f = open(file_path, "w", encoding="utf-8")
    for x in items:
        f.write(str(x) + "\n")
    f.close()
    print(Fore.CYAN + "Wrote list to", file_path)

def gen_AZ_files(path):
    i = 65
    while i <= 90:
        name = chr(i) + ".txt"
        full = os.path.join(path, name)
        f = open(full, "w", encoding="utf-8")
        f.write("This is file " + name + "\n")
        f.close()
        i = i + 1
    print(Fore.CYAN + "Generated A.txt..Z.txt in", path)

def copy_file(src, dst):
    s = open(src, "rb")
    data = s.read()
    s.close()
    d = open(dst, "wb")
    d.write(data)
    d.close()
    print(Fore.CYAN + "Copied", src, "to", dst)

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(Fore.GREEN + "Deleted:", file_path)
        else:
            print(Fore.RED + "No write permission to delete")
    else:
        print(Fore.RED + "No such file")
        
base = os.getcwd()
print(Fore.BLUE + "Base:", base)

list_only(base)
print()
check_access(base)
print()
demo_file = os.path.join(base, "demo.txt")
write_list(demo_file, ["apple", "banana", "cherry"])
print()
path_info(demo_file)
print()

count_lines(demo_file)
print()
gen_AZ_files(base)
print()
copy_file(demo_file, os.path.join(base, "demo_copy.txt"))
print()
delete_file(demo_file)




