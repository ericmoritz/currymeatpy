from currymeat import curry
import currymeat


@curry
def key(key, d, default=None):
    """Returns the value for a dictionary key"""
    return d.get(key, default)


@curry
def div(a, b):
    return a / b

def test_curry():
    foo = key("foo")
    assert foo({"foo": "bar"}) == "bar"
    assert foo({}, default="") == ""

    foo_int = key("foo", default=0)
    assert foo_int({"foo": 1}) == 1
    assert foo_int({}) == 0

    half = div(b=2)
    assert half(100) == 50.0


def test_needed_args():
    def foo(key, d, default=None):
        pass

    assert currymeat._needed_args(foo) == ['key', 'd']


def test_reduce_needed_args():
    assert (
        currymeat._reduce_needed_args(['key', 'd'], ('foo', ))
        == 
        ['d']
    )
    assert (
        currymeat._reduce_needed_args(['key', 'd'], ('foo', {})) 
        == 
        []    
    )
