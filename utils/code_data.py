CODE_SOLUTIONS = {
    "python": [
        {
            "prompts": [
                "add two numbers",
                "sum of two numbers using a function",
                "python function to add two integers"
            ],
            "code": "def add(a, b):\n    return a + b\n\na = int(input('Enter first number: '))\nb = int(input('Enter second number: '))\nprint('Sum is:', add(a, b))"
        },
        {
            "prompts": [
                "check if a number is even",
                "is the number even or odd?",
                "function to check even number"
            ],
            "code": "def is_even(n):\n    return n % 2 == 0\n\nn = int(input('Enter a number: '))\nprint('Even' if is_even(n) else 'Odd')"
        },
        {
            "prompts": [
                "generate fibonacci series",
                "fibonacci sequence up to n terms",
                "print n fibonacci numbers"
            ],
            "code": "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        print(a, end=' ')\n        a, b = b, a + b\n\nn = int(input('Enter number of terms: '))\nfibonacci(n)"
        },
        {
            "prompts": [
                "calculate factorial using recursion",
                "find factorial of a number",
                "recursive factorial function"
            ],
            "code": "def factorial(n):\n    return 1 if n == 0 else n * factorial(n - 1)\n\nn = int(input('Enter a number: '))\nprint('Factorial:', factorial(n))"
        },
        {
            "prompts": [
                "reverse a string in python",
                "function to reverse a string",
                "flip characters in a string"
            ],
            "code": "def reverse_string(s):\n    return s[::-1]\n\ns = input('Enter a string: ')\nprint('Reversed:', reverse_string(s))"
        },
        {
            "prompts": [
                "check palindrome string",
                "is the string a palindrome?",
                "palindrome check using python"
            ],
            "code": "def is_palindrome(s):\n    return s == s[::-1]\n\ns = input('Enter a string: ')\nprint('Palindrome' if is_palindrome(s) else 'Not a palindrome')"
        },
        {
            "prompts": [
                "square root of a number",
                "find sqrt using exponent",
                "sqrt without math module"
            ],
            "code": "def square_root(n):\n    return n ** 0.5\n\nn = float(input('Enter number: '))\nprint('Square root:', square_root(n))"
        },
        {
            "prompts": [
                "find maximum in a list",
                "get largest number in list"
            ],
            "code": "def find_max(lst):\n    return max(lst)\n\nprint(find_max([1, 5, 3, 9]))"
        },
        {
            "prompts": [
                "remove duplicate elements from list",
                "eliminate repeated values in list"
            ],
            "code": "def remove_duplicates(lst):\n    return list(set(lst))\n\nprint(remove_duplicates([1, 2, 2, 3, 4, 4]))"
        },
        {
            "prompts": [
                "sort a list in ascending order",
                "how to sort elements in python"
            ],
            "code": "def sort_list(lst):\n    return sorted(lst)\n\nprint(sort_list([3, 1, 4, 2]))"
        },
        {
            "prompts": [
                "count vowels in a string",
                "find number of vowels"
            ],
            "code": "def count_vowels(s):\n    return sum(1 for c in s.lower() if c in 'aeiou')\n\nprint(count_vowels('Hello World'))"
        },
        {
            "prompts": [
                "merge two dictionaries",
                "combine two dicts"
            ],
            "code": "def merge_dicts(d1, d2):\n    return {**d1, **d2}\n\nprint(merge_dicts({'a': 1}, {'b': 2}))"
        },
        {
            "prompts": [
                "check if number is prime",
                "determine if a number is prime"
            ],
            "code": "def is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nprint(is_prime(17))"
        },
        {
            "prompts": [
                "find length of a string without len",
                "manual count of string length"
            ],
            "code": "def custom_len(s):\n    count = 0\n    for _ in s:\n        count += 1\n    return count\n\nprint(custom_len('Hello'))"
        },
        {
            "prompts": [
                "calculate gcd of two numbers",
                "find greatest common divisor"
            ],
            "code": "def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\nprint(gcd(12, 18))"
        },
        {
            "prompts": [
                "reverse the words in a sentence",
                "flip sentence word order"
            ],
            "code": "def reverse_words(sentence):\n    return ' '.join(sentence.split()[::-1])\n\nprint(reverse_words('hello world from python'))"
        },
        {
            "prompts": [
                "convert celsius to fahrenheit",
                "temperature conversion"
            ],
            "code": "def celsius_to_fahrenheit(c):\n    return (c * 9/5) + 32\n\nprint(celsius_to_fahrenheit(37))"
        },
        {
            "prompts": [
                "frequency of characters in string",
                "count character occurrences"
            ],
            "code": "def char_frequency(s):\n    freq = {}\n    for char in s:\n        freq[char] = freq.get(char, 0) + 1\n    return freq\n\nprint(char_frequency('banana'))"
        },
        {
            "prompts": [
                "check if two strings are anagrams",
                "is one string an anagram of another?"
            ],
            "code": "def is_anagram(s1, s2):\n    return sorted(s1) == sorted(s2)\n\nprint(is_anagram('listen', 'silent'))"
        },
        {
            "prompts": [
                "flatten nested list",
                "convert nested lists into one list"
            ],
            "code": "def flatten(lst):\n    result = []\n    for i in lst:\n        if isinstance(i, list):\n            result.extend(flatten(i))\n        else:\n            result.append(i)\n    return result\n\nprint(flatten([1, [2, [3, 4], 5], 6]))"
        },
        {
            "prompts": [
                "find second largest in list",
                "get 2nd highest number from list"
            ],
            "code": "def second_largest(lst):\n    unique = sorted(set(lst))\n    return unique[-2] if len(unique) >= 2 else None\n\nprint(second_largest([1, 3, 5, 2, 4]))"
        },
        {
            "prompts": [
                "convert number to binary",
                "decimal to binary converter"
            ],
            "code": "def to_binary(n):\n    return bin(n)[2:]\n\nprint(to_binary(10))"
        },
        {
            "prompts": [
                "check uniqueness of list elements",
                "are all list elements unique?"
            ],
            "code": "def all_unique(lst):\n    return len(lst) == len(set(lst))\n\nprint(all_unique([1, 2, 3, 4, 5]))"
        },
        {
            "prompts": [
                "sum of digits of number",
                "calculate digit total"
            ],
            "code": "def sum_of_digits(n):\n    return sum(int(d) for d in str(n))\n\nprint(sum_of_digits(1234))"
        },
        {
            "prompts": [
                "find nth fibonacci number",
                "recursive fibonacci nth value"
            ],
            "code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(fibonacci(7))"
        },
        {
            "prompts": [
                "capitalize first letter of each word",
                "title case a sentence"
            ],
            "code": "def capitalize_words(s):\n    return ' '.join(word.capitalize() for word in s.split())\n\nprint(capitalize_words('hello world'))"
        },
        {
            "prompts": [
                "generate list of squares from 1 to n",
                "square of first n natural numbers"
            ],
            "code": "def generate_squares(n):\n    return [i ** 2 for i in range(1, n + 1)]\n\nprint(generate_squares(5))"
        }
    ]
}
