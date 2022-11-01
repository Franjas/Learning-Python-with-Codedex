# Create a program and think of a theme for the songs.
# Define a playlist list and throw in some songs.
# Now loop over the list and print everything out!
# Try different ways to do so before moving on.
# Codédex

playlist = ['Porches - Rangerover',
            'Mount Eerie - You Swan Go On',
            'Caroline Polachek - Look at Me Now',
            'Pinegegrove - Darkness',
            'LVP UP - Spirit Was',
            'First Love - Late Spring']
print(playlist)
#######################################
playlist.append('Yeah Yeah Yeah - Heads Will Roll')
print(playlist)
#######################################
playlist.insert(4, 'Perfume Genius - Queen')
print(playlist)
#######################################
playlist.reverse()
print(playlist)
#######################################
playlist = playlist.index('LVP UP - Spirit Was')
print(playlist)

#for song in playlist:
#    print(song)