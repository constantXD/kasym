import math
import time

numbers = [2, 3, 4, 5]
result = math.prod(numbers)
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

import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

number = int(input())
delay = int(input())
result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

number = int(input())
delay = int(input())

result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

tup = (True, True, False)
print(all(tup))

import os
from colorama import Fore
import sys, tty, termios
import string

def list_files_directories(path):
    print(Fore.CYAN + "Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print(Fore.GREEN + "\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    
    print(Fore.YELLOW + "\nAll files and directories:")
    for item in os.listdir(path):
        print(item)

def check_access(path):
    exists = os.path.exists(path)
    if exists:
        print(f"{Fore.GREEN}Path exists: {path}")
        print(f"Readable: {os.access(path, os.R_OK)}")
        print(f"Writable: {os.access(path, os.W_OK)}")
        print(f"Executable: {os.access(path, os.X_OK)}")
    else:
        print(f"{Fore.RED}Path does not exist: {path}")

def test_path_exists(path):
    if os.path.exists(path):
        print(f"{Fore.GREEN}Path exists: {path}")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"{Fore.RED}Path does not exist: {path}")

def count_lines_in_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        print(f"{Fore.YELLOW}Number of lines: {len(lines)}")

def write_list_to_file(filepath, my_list):
    with open(filepath, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")

def copy_file(src, dst):
    try:
        with open(src, 'r') as fsrc, open(dst, 'w') as fdst:
            fdst.write(fsrc.read())
        print(f"{Fore.CYAN}File copied from {src} to {dst}")
    except FileNotFoundError:
        print(f"{Fore.RED}File not found.")
    except PermissionError:
        print(f"{Fore.RED}Permission denied.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{Fore.GREEN}File {path} deleted successfully.")
        else:
            print(f"{Fore.RED}File {path} is not writable.")
    else:
        print(f"{Fore.RED}File {path} does not exist.")

path = '/your/directory/path'
filepath = '/your/directory/path/file.txt'

list_files_directories(path)
check_access(path)
test_path_exists(filepath)
count_lines_in_file(filepath)

my_list = ["apple", "banana", "cherry"]
write_list_to_file(filepath, my_list)

generate_files()

src = '/your/directory/path/source.txt'
dst = '/your/directory/path/destination.txt'
copy_file(src, dst)

delete_file(filepath)
