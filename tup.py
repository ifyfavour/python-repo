afro_beat_artists = ('Davido', 'wizkid', 'Tiwa Savage', 'Flavour', 'Python')
print(afro_beat_artists[3])
print(afro_beat_artists[-3])
print(afro_beat_artists[0:2])

y = list(afro_beat_artists)
y.append('Omahlay')
afro_beat_artists = tuple(y)
print(afro_beat_artists)
another_afro_beat_artist = ('Odumodu Blak',)
afro_beat_artists += another_afro_beat_artist
print(afro_beat_artists)
a = 0
