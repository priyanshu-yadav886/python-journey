from pathlib import Path

path = Path('Excercises_from_PythonCrashCourse/learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace('python', 'java'))
    