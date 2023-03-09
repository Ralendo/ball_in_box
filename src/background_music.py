import pygame
import glob


# Music init
def start_play_music():
    tracklist = []
    for f in glob.glob("music/*.wav"):
        tracklist.append(f)
    current_tracklist = tracklist
    print('Music added..')
    pygame.mixer.music.load(current_tracklist[0])
    pygame.mixer.music.play()
    current_tracklist.pop(0)
    pygame.mixer.music.queue(current_tracklist[0])
    current_tracklist.pop(0)
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)
    return current_tracklist, tracklist, MUSIC_END

def play_music(current_tracklist, tracklist, MUSIC_END):
    for event in pygame.event.get():
        # Music next and repeat tracks
        if event.type == MUSIC_END:
            print('Song finished..')
            if len(current_tracklist) > 0:
                pygame.mixer.music.queue(current_tracklist[0])
                current_tracklist.pop()
        if not pygame.mixer.music.get_busy():
            print('Playlist refreshing..')
            current_tracklist = tracklist
        return current_tracklist
