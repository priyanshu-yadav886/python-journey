from pathlib import Path
content = input("Write your name: ")
path = Path('Excercises_from_PythonCrashCourse/guest.txt')
path.write_text(content)