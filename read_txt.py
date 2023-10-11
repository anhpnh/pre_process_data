from bing_image_downloader import downloader

filename = './undownload/pho_bien_vietnam.txt'

with open(filename) as file:
    for line in file:
        str = f'{line.rstrip()}'
        print(
              f'########################################################################################################')
        print(f'############################### Searching ... {str}######################################################')
        print(
            f'########################################################################################################')
        downloader.download(str, limit=100, output_dir='dataset', adult_filter_off=True,
                            force_replace=False, timeout=5, verbose=True)