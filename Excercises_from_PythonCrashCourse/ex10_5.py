from pathlib import Path

path = Path('Excercises_from_PythonCrashCourse/guest_book.txt')

prompt = "Write your name."
prompt += "Write 'quit' if you are the last guest."

guest_book = []

while True:
    content = input(prompt)

    if content == 'quit':
        break

    print(f"\nThanks {content}, I'll add your name to guest list.")
    guest_book.append(content)

f_string = ' '
for name in guest_book:
    f_string += f"{name}\n"

    
path.write_text(f_string)