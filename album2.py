def make_album(artist_name, album_title):
    "Return an artist and an album name"
    album = f"{artist_name} {album_title}"
    return album.title()
while True:
    print(f"\nPlease tell me artist name: ")
    print(f"\nEnter 'q' at anytime you want to quit")
    a_name = input("Artist Name: ")
    if a_name == 'q':
        break
    al_name = input(f"\nEnter Album Name: ")
    if al_name == 'q':
        break
    music = make_album(a_name, al_name)
    print(music)