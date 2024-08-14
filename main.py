import builtins
from argument_parser import parse_arguments
from youtube_downloader import download_youtube_playlist
from spotify_downloader import download_spotify_playlist
from tqdm import tqdm

def main():
    original_print = builtins.print
    builtins.print = tqdm.write

    try:
        args = parse_arguments()
        if args.platform == 'youtube':
            download_youtube_playlist(args.url, args.output)
        elif args.platform == 'spotify':
            download_spotify_playlist(args.url, args.output)
    finally:
        builtins.print = original_print  # Restore original print function

if __name__ == "__main__":
    main()
