from pathlib import Path
import os

path_folder_playlist_phone = '/mnt/0CD4B8BFD4B8ABF8/Music/.Playlists (Phone)'
path_folder_playlist_computer = '/mnt/0CD4B8BFD4B8ABF8/Music/.Playlists (Computer-Linux)'
path_phone = '/storage/emulated/0/Music/'
path_computer = '/mnt/0CD4B8BFD4B8ABF8/Music/'

if not os.path.exists(path_folder_playlist_computer):
    os.makedirs(path_folder_playlist_computer)

for path_playlist in Path(path_folder_playlist_computer).iterdir():
    path_playlist.unlink(missing_ok=True)  # remove old playlists

for path_playlist in Path(path_folder_playlist_phone).iterdir():
    path_playlist_new = path_folder_playlist_computer + str(path_playlist)[len(path_folder_playlist_phone):]
    print(f'Processing {path_playlist_new}')
    with open(path_playlist_new, 'w', encoding='utf8') as file_dest:
        line_list = (line for line in open(path_playlist, 'r', encoding='utf8')
                     if line[0] != '#')  # ratings are prepended with #

        for line in line_list:
            line = path_computer + line[len(path_phone):]
            print(f'Changing to {line}')

            file_dest.write(line + '\n')
