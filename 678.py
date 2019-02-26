import os
import sys
from time import time

FILE = 'rwtest'

def write_test(file, size_bytes):
    f = os.open(file, os.O_CREAT | os.O_WRONLY)
    data = os.urandom(size_bytes)
    start_time = time() * 1000
    os.write(f, data)
    os.fsync(f)
    end_time = time() * 1000
    os.close(f)
    return end_time - start_time

def read_test(file, size_bytes):
    f = os.open(file, os.O_RDONLY)
    start_time = time() * 1000
    data = os.read(f, size_bytes)
    end_time = time() * 1000
    os.close(f)
    return end_time - start_time

def test(file, size, unit):
    size_bytes = size
    if unit.lower() == 'kb':
        size_bytes *= 1024
    elif unit.lower() == 'mb':
        size_bytes *= 1024 * 1024
    elif unit.lower() == 'gb':
        size_bytes *= 1024 * 1024 * 1024

    print('----------Storage Performance Test----------')

    wt = write_test(file, size_bytes)
    avg_ws = float(size_bytes) / wt
    print("Write %d %s in %.2f ms." % (size, unit.upper(), wt))
    print("Average writing speed: %.2f Bytes / ms" % (avg_ws))

    print('---------------------------------------------------')

    rt = read_test(file, size_bytes)
    avg_rs = float(size_bytes) / rt
    print("Read %d %s in %.2f ms." % (size, unit.upper(), rt))
    print("Average reading speed: %.2f Bytes / ms" % (avg_rs))

    os.remove(file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage error, pls try again.') # parameters check, not that comprehensive
    else:
        size = int(sys.argv[1])
        unit = sys.argv[2]

        test(FILE, size, unit)
