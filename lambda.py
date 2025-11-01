numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = lambda x: x % 2 == 0

even_numbers = list(filter(is_even, numbers))


print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

data = [("apple", 2), ("banana", 3), ("cherry", 1), ("date", 4)]

sorted_data = sorted(data, key=lambda item: item[1], reverse=True)
print(f"Sorted dat: {sorted_data}")


import datetime

now = datetime.datetime.now()
print(f"Current datetime: {now}")


my_date = datetime.date(2025, 12, 25)
print(f"My date: {my_date}")

my_time = datetime.time(10, 30, 0)
print(f"My time: {my_time}")

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")
