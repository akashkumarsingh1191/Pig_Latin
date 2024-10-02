from Ascii_art import logo
# print(logo)
# a program which simulates very simpe Music APP.

'''
    1. Create Nested Tuple with given song list. 
    - Green Day
            1. Somewhere Now
            2. Bang Bang
            3. Revolution Radio
            4. Say Goodbye
            5. Outlaws
    - Metallica
            1. Battery
            2. Master of Puppets
            3. The Thing That Should Not Be
            4. Welcome Home (Sanitarium)
    - U2
            1. The Miracle
            2. Every Breaking Wave
            3. California
            4. Song for Someone
            5. Iris (Hold Me Close)

2. Show Ascii art logo
3. Print Song list
4. Ask from user to select a song based on number (1:1). First digit is band number and second digit is song number. For example 1:1 means first band and first song which is "Green Day Somewhere" Now in our case.
 5. Playing song and asking if a user want to select different song or not. If not app terminates.
'''

from music import playlist

# print(playlist[0])
# print(playlist[0][1])
# print(playlist[0][1][0])
# print(playlist[0][1][0][1])


# print(playlist[1])
# print(playlist[1][1])
# print(playlist[1][1][1])
# print(playlist[1][1][1][0])

def print_playlist():
        for b_index ,band in enumerate(playlist,1):
                name,songs=band
                for song_num,song in songs:
                        print(f'{b_index}:{song_num} {name} - {song}')
# print_playlist()

def print_song(p_bnumber,p_snumber):
        band_name=playlist[p_bnumber-1][0]
        song_name=playlist[p_bnumber-1][1][p_snumber-1][1]
        print(f"\n{band_name} - {song_name} playing now...")
while True:
        print_playlist()
        current_play=input("\nSelect a song to play using number:(1:1) ")
        band_number=int(current_play[0])
        song_number=int(current_play[2])
        print_song(band_number,song_number)
        change=input("\nPress C to change the song or any key to quit App: ")
        if change =="C":
                continue
        break
print("Good bye! ")