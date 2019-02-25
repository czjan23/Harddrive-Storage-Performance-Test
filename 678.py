import os
import sys
from time import time

FILE = 'rwtest'

def write_test(file, total_size_mb):
    f = os.open(file, os.O_CREAT | os.O_WRONLY)
    size_bytes = total_size_mb * 1024 * 1024
    data = os.urandom(size_bytes)
    start_time = time() * 1000
    os.write(f, data)
    os.fsync(f)
    end_time = time() * 1000
    os.close(f)
    t = end_time - start_time
    print("Write %d MB in %.2f ms." % (total_size_mb, t))

def read_test(file, total_size_mb):
    f = os.open(file, os.O_RDONLY)
    size_bytes = total_size_mb * 1024 * 1024
    start_time = time() * 1000
    data = os.read(f, size_bytes)
    end_time = time() * 1000
    os.close(f)
    t = end_time - start_time
    print("Read %d MB in %.2f ms." % (total_size_mb, t))

def test(file, size):
    write_test(file, size)
    read_test(file, size)
    os.remove(file)

if __name__ == "__main__":
    size_mb = int(sys.argv[1])
    test(FILE, size_mb)
