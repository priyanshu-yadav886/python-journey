favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

poll = ['jen', 'sarah', 'prince', 'anuj']

for name in poll:
    if name in favorite_languages:
        print(f"Thank You {name.title()} for responding.")

    else:
        print(f"{name},please take the poll.")