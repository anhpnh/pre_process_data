import argparse
from bing_image_downloader import downloader


parser = argparse.ArgumentParser()
parser.add_argument('--str', nargs='*', type=str, help='string Toyota, Chevrolet...')
parser.add_argument('--models', nargs='*', type=str, help='txt file models')
args = parser.parse_args()

str_model = args.str[0]
filename = args.models[0]
#print(str_model, filename)

with open(filename) as file:
    for line in file:
        str = f'{str_model} {line.rstrip()}'
        print(f'################# Searching ... {str} ##########################')
        downloader.download(str, limit=100, output_dir='dataset', adult_filter_off=True,
                            force_replace=False, timeout=5, verbose=True)

