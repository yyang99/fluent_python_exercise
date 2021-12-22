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
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        # res = executor.map(download_one, sorted(cc_list))
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f"Scheculed for {cc}: {future}")

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print(f'{future} return: {res!r}')
            results.append((res))

    return len(results)


if __name__ == '__main__':
    main(download_many)
