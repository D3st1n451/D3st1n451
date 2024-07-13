from datetime import date
user_name = input()
user_age = int(input())

current_year = date.today().year
birth_year = current_year - user_age

print("What is your name?", user_name)
print("How old are you?", user_age)
print('Hello {name}! You were born in {year}.'.format(name=user_name, year=birth_year))
