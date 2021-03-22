from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists('data'):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


if __name__ == '__main__':
    feed = load()
    print(f"{feed['Schedule'].keys()=}")
    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))

    print(f"{feed['Schedule']['speakers'][-1]['name']=}")
    print(f"{feed['Schedule']['speakers'][-1]['serial']=}")
    print(f"{feed['Schedule']['events'][40]['name']=}")
    print(f"{feed['Schedule']['events'][40]['speakers']=}")
