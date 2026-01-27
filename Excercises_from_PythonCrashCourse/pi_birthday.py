from pathlib import Path

path = Path('Excercises_from_PythonCrashCourse/pi_million_digits.txt')
contents = path.read_text()

pi_strings = ' '

for line in contents.splitlines():
    pi_strings += line.lstrip()


birthday = input("Input Your birthday: ")

if birthday in pi_strings:
    print("Your birthday is in pi.")

else:
    print("Your birthday is not in pi.")