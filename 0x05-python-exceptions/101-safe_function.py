#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    val = None
    try:
        val = fct(*args)
    except Exception as err:
        print("Exception:", err, file=stderr)
    finally:
        return val
