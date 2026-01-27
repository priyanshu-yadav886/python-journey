def make_album(artist_name, album_title, no_of_songs = None):
    "Return a dictionary for a music album"
    album = {'artist' : artist_name, 'number of songs' : no_of_songs, 'album name' : album_title}
    if no_of_songs:
        album['number of songs'] = no_of_songs
    return album

music = make_album('coldplay', 'ghost stories', '6')
print(music)