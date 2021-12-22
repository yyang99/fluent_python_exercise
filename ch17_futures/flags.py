import os
import sys
import time
from typing import List

import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VM ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads'

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc: str):
    url = f"{BASE_URL}/{cc.lower()}.gif'"
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list: List[str]):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, f'{cc.lower()}.gif')
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n{count} flags downloaded in {elapsed:.2f}s')


if __name__ == '__main__':
    main(download_many)
