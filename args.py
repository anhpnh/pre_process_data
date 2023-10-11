import argparse
from bing_image_downloader import downloader

def main(str):
    downloader.download(f'Toyota {str}', limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


parser = argparse.ArgumentParser()
parser.add_argument('--str', nargs='*', type=str, help='string for keyword Bing search')
args = parser.parse_args()

print(args.str[0])

main(args.str[0])