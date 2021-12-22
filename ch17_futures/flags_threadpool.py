from concurrent import futures
from typing import List

from flags import get_flag, show, save_flag, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, f'{cc.lower()}.gif')
    return cc


def download_many(cc_list: List[str]):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(cc_list)


if __name__ == '__main__':
    main(download_many)
