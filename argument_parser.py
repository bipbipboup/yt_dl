import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Download a playlist as m4a files.')
    parser.add_argument('url', type=str, help='The URL of the playlist (YouTube or Spotify)')
    parser.add_argument('--output', type=str, default=None, help='The directory to save the m4a files')
    parser.add_argument('--platform', type=str, choices=['youtube', 'spotify'], required=True,
                        help='The platform to download from: youtube or spotify')
    return parser.parse_args()
