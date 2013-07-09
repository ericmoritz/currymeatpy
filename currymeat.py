import inspect
from functools import wraps
        
def curry(fn, *init_args, **init_keywords):
    needed_args = _needed_args(fn)
    return _curry(fn, needed_args, init_args, init_keywords)


def _curry(fn, init_needed_args, init_args, init_keywords):
    def inner(*args, **keywords):
        args = _merge_args(init_args, args)
        keywords = _merge_keywords(init_keywords, keywords)
        needed_args = _reduce_needed_args(init_needed_args, args)

        if not needed_args:
            return fn(*args, **keywords)
        else:
            return _curry(fn, needed_args, args, keywords)
    inner.__name__ = fn.__name__
    inner.__module__ = fn.__module__
    inner.__doc__ = fn.__doc__
    return inner    


def _needed_args(fn):
    s = inspect.getargspec(fn)
    if s.defaults:
        # chop off the defaults from the args
        return s.args[:len(s.defaults)*-1]
    else:
        return s.args

def _reduce_needed_args(needed_args, args):
    return needed_args[len(args):]

    
def _merge_keywords(keywords1, keywords2):
    return dict(keywords1, **keywords2)


def _merge_args(args1, args2):
    return args1 + args2

