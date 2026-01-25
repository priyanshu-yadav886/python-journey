from pathlib import Path
content = input("Write your name: ")
path = Path('guest.txt')
path.write_text(content)