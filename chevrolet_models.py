from bing_image_downloader import downloader

filename = './chevrolet_models.txt'

with open(filename) as file:
    for line in file:
        str = f'Chevrolet {line.rstrip()}'
        print(f'Searching ... {str}')
        downloader.download(str, limit=100, output_dir='dataset', adult_filter_off=True,
                            force_replace=False, timeout=60, verbose=True)