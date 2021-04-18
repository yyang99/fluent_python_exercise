from exercise.ch21_class_metaprog.record_factory import record_factory

def test_record_factory():
    Dog = record_factory('Dog', 'name weight owner')
    rex = Dog('Rex', 30, 'Bob')
    print(f"{rex=}")
    name, weight, _ = rex
    assert (name, weight) == ('Rex', 30)
    print("{2}'s dog weights {1}kg".format(*rex))
    rex.weight = 32
    print(f"{Dog.__mro__=}")
    _, weight, _ = rex
    assert weight == 32
