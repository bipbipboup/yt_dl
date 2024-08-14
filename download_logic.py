import os
from yt_dlp import YoutubeDL
from tqdm import tqdm
from filename_utils import create_output_directory


def download_playlist(playlist_info, output_path, platform, download_func):
    """Downloads all tracks in a playlist using the specified download function."""
    total_tracks = len(playlist_info['entries'])

    print(f"📂 Downloading {platform} playlist: '{playlist_info['title']}' ({total_tracks} tracks) in {output_path}")
    
    for track_info in tqdm(playlist_info['entries'], desc="Progress", unit="track"):
        track_url = track_info['url']  # Adapt this based on platform-specific structure
        download_func(track_url, output_path, platform)

    print(f"✅ All tracks in the {platform} playlist '{playlist_info['title']}' have been processed.")
