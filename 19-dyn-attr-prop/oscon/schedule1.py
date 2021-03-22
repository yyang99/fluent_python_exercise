import warnings
import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db_record = Record(**record)
            db[key] = db_record

if __name__ == '__main__':
    import shelve
    db = shelve.open((DB_NAME))
    if CONFERENCE not in db:
        load_db(db)

    speaker = db['speaker.3471']
    print(f'{type(speaker)=}')
    print(f'{speaker.name=} {speaker.twitter=}')

    db.close()