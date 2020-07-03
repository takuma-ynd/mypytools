from contextlib import contextmanager
import time
from misc import print_green

@contextmanager
def timed(name):
    start = time.time()
    yield
    elapsed = time.time() - start
    if elapsed < 1.0:
        print_green(name + ' is finished in {:.0f} ms'.format(elapsed * 1000))
    else:
        print_green(name + ' is finised in {:.0f} sec ({:.1f} min)'.format(elapsed, elapsed / 60))
