# Task 1: Create a generator to iterate over a list of numbers.
def list_iterator(numbers):
    for number in numbers:
        yield number

# Task 2: Develop a generator that yields even numbers from a given range.
def even_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

# Task 3: Implement a generator to yield odd numbers within a specified range.
def odd_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

# Task 4: Write a generator that produces Fibonacci numbers.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5: Create a generator that yields prime numbers up to a given limit.
def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number

# Task 6: Develop a generator to traverse a binary tree in pre-order.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

# Task 7: Implement a generator for in-order traversal of a binary tree.
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

# Task 8: Write a generator for post-order traversal of a binary tree.
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

# Task 9: Create a generator to traverse a graph using depth-first search (DFS).
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

# Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            queue.extend(graph[vertex])

# Task 11: Implement a generator that yields the keys of a dictionary.
def dict_keys_generator(d):
    for key in d.keys():
        yield key

# Task 12: Write a generator that yields the values of a dictionary.
def dict_values_generator(d):
    for value in d.values():
        yield value

# Task 13: Create a generator to iterate over key-value pairs of a dictionary.
def dict_items_generator(d):
    for item in d.items():
        yield item

# Task 14: Develop a generator that yields lines from a file one by one.
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 15: Implement a generator to iterate over words in a text file.
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16: Write a generator that yields characters from a string one by one.
def string_chars_generator(s):
    for char in s:
        yield char

# Task 17: Create a generator to yield unique elements from a list.
def unique_elements_generator(lst):
    seen = set()
    for element in lst:
        if element not in seen:
            seen.add(element)
            yield element

# Task 18: Develop a generator that yields elements of a list in reverse order.
def reverse_list_generator(lst):
    for element in reversed(lst):
        yield element

# Task 19: Implement a generator to yield the Cartesian product of two lists.
def cartesian_product_generator(lst1, lst2):
    for element1 in lst1:
        for element2 in lst2:
            yield (element1, element2)

# Task 20: Write a generator that yields permutations of a list.
def permutations_generator(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in permutations_generator(lst[:i] + lst[i+1:]):
                yield [lst[i]] + perm

# Task 21: Create a generator to yield combinations of a list of elements.
def combinations_generator(lst):
    if len(lst) == 0:
        yield []
    else:
        for combination in combinations_generator(lst[1:]):
            yield combination
            yield [lst[0]] + combination

# Task 22: Develop a generator to iterate over a list of tuples.
def tuple_list_generator(lst):
    for t in lst:
        yield t

# Task 23: Implement a generator that yields elements from multiple lists in parallel.
def parallel_lists_generator(*lists):
    for elements in zip(*lists):
        yield elements

# Task 24: Write a generator that yields elements from a nested list (flattening the list).
def nested_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from nested_list_generator(element)
        else:
            yield element

# Task 25: Create a generator to yield elements from a nested dictionary.
def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

# Task 26: Develop a generator to yield powers of 2 up to a given number.
def powers_of_2_generator(n):
    i = 1
    while i <= n:
        yield i
        i *= 2

# Task 27: Implement a generator that yields powers of a given base up to a specified limit.
def powers_of_base_generator(base, limit):
    i = 1
    while i <= limit:
        yield i
        i *= base

# Task 28: Write a generator to yield the squares of numbers in a given range.
def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2

# Task 29: Create a generator to yield cubes of numbers in a specified range.
def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3

# Task 30: Develop a generator that yields factorials of numbers up to a given limit.
def factorials_generator(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)
    
    for i in range(n + 1):
        yield factorial(i)

# Task 31: Implement a generator to yield numbers in the Collatz sequence.
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1

# Task 32: Write a generator that yields numbers in a geometric progression.
def geometric_progression_generator(start, ratio, limit):
    current = start
    while current <= limit:
        yield current
        current *= ratio

# Task 33: Create a generator to yield numbers in an arithmetic progression.
def arithmetic_progression_generator(start, difference, limit):
    current = start
    while current <= limit:
        yield current
        current += difference

# Task 34: Develop a generator that yields the running sum of a list of numbers.
def running_sum_generator(lst):
    running_sum = 0
    for number in lst:
        running_sum += number
        yield running_sum

# Task 35: Implement a generator to yield the running product of a list of numbers.
def running_product_generator(lst):
    running_product = 1
    for number in lst:
        running_product *= number
        yield running_product

# Example usage of some of the generators
if __name__ == "__main__":
    # Task 1
    print(list(list_iterator([1, 2, 3, 4, 5])))

    # Task 2
    print(list(even_generator(1, 10)))

    # Task 3
    print(list(odd_generator(1, 10)))

    # Task 4
    fib_gen = fibonacci_generator()
    print([next(fib_gen) for _ in range(10)])

    # Task 5
    print(list(prime_generator(20)))

    # Task 6-8: Binary tree example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(list(pre_order_traversal(root)))
    print(list(in_order_traversal(root)))
    print(list(post_order_traversal(root)))

    # Task 9-10: Graph example
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print(list(dfs(graph, 'A')))
    print(list(bfs(graph, 'A')))

    # Task 11-13: Dictionary example
    d = {'a': 1, 'b': 2, 'c': 3}
    print(list(dict_keys_generator(d)))
    print(list(dict_values_generator(d)))
    print(list(dict_items_generator(d)))

    # Task 14-15: File example (uncomment to run with a valid file path)
    # print(list(file_lines_generator('example.txt')))
    # print(list(file_words_generator('example.txt')))

    # Task 16
    print(list(string_chars_generator("Hello")))

    # Task 17
    print(list(unique_elements_generator([1, 2, 2, 3, 4, 4, 5])))

    # Task 18
    print(list(reverse_list_generator([1, 2, 3, 4, 5])))

    # Task 19
    print(list(cartesian_product_generator([1, 2], ['a', 'b'])))

    # Task 20
    print(list(permutations_generator([1, 2, 3])))

    # Task 21
    print(list(combinations_generator([1, 2, 3])))

    # Task 22
    print(list(tuple_list_generator([(1, 2), (3, 4), (5, 6)])))

    # Task 23
    print(list(parallel_lists_generator([1, 2], ['a', 'b'], [True, False])))

    # Task 24
    print(list(nested_list_generator([1, [2, 3], [4, [5, 6]]])))

    # Task 25
    nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
    print(list(nested_dict_generator(nested_dict)))

    # Task 26
    print(list(powers_of_2_generator(16)))

    # Task 27
    print(list(powers_of_base_generator(3, 81)))

    # Task 28
    print(list(squares_generator(1, 5)))

    # Task 29
    print(list(cubes_generator(1, 5)))

    # Task 30
    print(list(factorials_generator(5)))

    # Task 31
    print(list(collatz_sequence_generator(13)))

    # Task 32
    print(list(geometric_progression_generator(1, 2, 16)))

    # Task 33
    print(list(arithmetic_progression_generator(1, 3, 10)))

    # Task 34
    print(list(running_sum_generator([1, 2, 3, 4])))

    # Task 35
    print(list(running_product_generator([1, 2, 3, 4])))
