import os
from yt_dlp import YoutubeDL
from filename_utils import sanitize_filename, create_output_directory
from download_logic import download_playlist


def download_youtube_track_as_m4a(track_url, output_path, platform):
    """Downloads a single track as m4a, depending on the platform."""
    try:
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(track_url, download=False)
            output_file = ydl.prepare_filename(info_dict)
            
            if os.path.exists(output_file):
                print(f"✔️ File already exists: '{os.path.basename(output_file)}'. Skipping download.")
            else:
                print(f"⬇️ Downloading: '{info_dict.get('title', 'Unknown Title')}' from {platform}")
                ydl.download([track_url])

    except Exception as e:
        print(f"❌ Error downloading '{track_url}' from {platform}: {e}")


def download_youtube_playlist(playlist_url, output_path):
    """Downloads all videos in a YouTube playlist as m4a files."""
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            playlist_info = ydl.extract_info(playlist_url, download=False)
        except Exception as e:
            print(f"❌ Failed to retrieve playlist information: {e}")
            return

    if not playlist_info or 'entries' not in playlist_info:
        print("❌ Failed to retrieve playlist entries.")
        return

    if not playlist_info['entries']:
        print(f"❌ The playlist '{playlist_info.get('title', 'Untitled Playlist')}' contains no videos.")
        return

    playlist_title = sanitize_filename(playlist_info.get("title", "Untitled Playlist"))

    if not output_path:
        output_path = playlist_title

    create_output_directory(output_path)

    # Download all tracks in the playlist
    download_playlist(playlist_info, output_path, 'YouTube', download_youtube_track_as_m4a)
