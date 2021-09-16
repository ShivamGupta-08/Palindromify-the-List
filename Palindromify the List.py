def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]
list_of_numbers = []
numbers_of_items = int(input("Enter the number integers you want to enter\n"))
for x in range(numbers_of_items):
    items_of_list = int(input("Enter your integer\n"))
    list_of_numbers.append(items_of_list)
for i in range(numbers_of_items):

    output_list = [list_of_numbers[i] if list_of_numbers[i]<10 else next_palindrome(list_of_numbers[i]) for i
                           in range(numbers_of_items)]
print(f"Your list : {list_of_numbers}")
print(f"Output list : {output_list}")
