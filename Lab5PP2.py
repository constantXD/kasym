import re

def tack1():
    pattern = r'a[b]*'
    test_strings = []
    for i in range(5):
        l = input()
        test_strings.append(l)
    for test in test_strings:
        if re.fullmatch(pattern, test):
            print(f'Match found: {test}')
        else:
            print(f'No match: {test}')

def tack2():
    pattern = r'ab{2,3}'
    test_strings = ['abb', 'abbb', 'abbbb', 'ab']
    for test in test_strings:
        if re.fullmatch(pattern, test):
            print(f'Match found: {test}')
        else:
            print(f'No match: {test}')

def tack3():
    pattern = r'[a-z]+(?:_[a-z]+)*'
    test_strings = ['hello_world', 'hello', 'hello_world_test', 'Hello_world']
    for test in test_strings:
        if re.fullmatch(pattern, test):
            print(f'Match found: {test}')
        else:
            print(f'No match: {test}')

def tack4():
    pattern = r'[A-Z][a-z]+'
    test_strings = ['Hello', 'HELLO', 'world', 'Hi']
    for test in test_strings:
        if re.fullmatch(pattern, test):
            print(f'Match found: {test}')
        else:
            print(f'No match: {test}')

def tacck5():
    pattern = r'a.*b'
    test_strings = ['ab', 'acb', 'abb', 'a123b', 'acb123b']
    for test in test_strings:
        if re.fullmatch(pattern, test):
            print(f'Match found: {test}')
        else:
            print(f'No match: {test}')

def tack6():
    pattern = r'[ ,.]'
    text = "Hello, world. How are you?"
    modified_text = re.sub(pattern, ':', text)
    print(f'Modified text: {modified_text}')

def tack7():
    text = "snake_case_string_example"
    camel_case = ''.join(word.capitalize() for word in text.split('_'))
    camel_case = camel_case[0].lower() + camel_case[1:]
    print(f'Camel case: {camel_case}')

def tack8():
    text = "SplitThisStringAtUppercaseLetters"
    result = re.findall(r'[A-Z][a-z]*', text)
    print(f'Splitted result: {result}')

def tack9():
    text = "InsertSpacesBetweenCapitalLetters"
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    print(f'Modified text: {modified_text}')

def tack10():
    text = "camelCaseStringExample"
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text).lower()
    print(f'Snake case: {snake_case}')