import os
import sys
import statistics
import math
from time import time

FILE = 'rwtest' # temp file, for write & read

def write_test(file, size_bytes):
    """Write performance test

    Parameters
    ----------
    file : str
        The file name for the temporary created file
    size_bytes : int
        A number specify the size of data to write in bytes

    Returns
    -------
    float
        A float number that is the time spent to write.
    """

    f = os.open(file, os.O_CREAT | os.O_WRONLY)
    data = os.urandom(size_bytes) # create random data with size_bytes in bytes
    start_time = time() * 1000
    os.write(f, data)
    os.fsync(f) # force os write to disk
    end_time = time() * 1000
    os.close(f)
    return end_time - start_time

def read_test(file, size_bytes):
    """Read performance test

    Parameters
    ----------
    file : str
        The file name for the temporary created file
    size_bytes : int
        A number specify the size of data to read in bytes

    Returns
    -------
    float
        A float number that is the time spent to read.
    """

    f = os.open(file, os.O_RDONLY)
    start_time = time() * 1000
    data = os.read(f, size_bytes)
    end_time = time() * 1000
    os.close(f)
    return end_time - start_time

def test(file, size, unit):
    """Test storage performance and print results

    Parameters
    ----------
    file : str
        The file name for the temporary created file
    size : int
        The number of [unit] that is going to read/write
    unit : str
        The data unit. Should be one of b, kb, mb, and gb.
    """

    size_bytes = size
    if unit.lower() == 'kb':
        size_bytes *= 1024
    elif unit.lower() == 'mb':
        size_bytes *= 1024 * 1024
    elif unit.lower() == 'gb':
        size_bytes *= 1024 * 1024 * 1024

    result = list()
    print('----------Storage Performance Test----------')

    wt = write_test(file, size_bytes)
    avg_ws = float(size_bytes) / wt
    result.append(avg_ws)
    print("Write %d %s in %.2f ms." % (size, unit.upper(), wt))
    print("Average writing speed: %.2f Bytes / ms" % (avg_ws))

    print('---------------------------------------------------')

    rt = read_test(file, size_bytes)
    avg_rs = float(size_bytes) / rt
    result.append(avg_rs)
    print("Read %d %s in %.2f ms." % (size, unit.upper(), rt))
    print("Average reading speed: %.2f Bytes / ms" % (avg_rs))

    print('----------------End Of Test-----------------')

    os.remove(file)
    return result

if __name__ == "__main__":
    """First do a parameters check. If the parameters are valid, do read/write test

    Parameters
    ----------
    argv[0] : str
        file name
    argv[1] : int
        number of [unit(argv[2])] that is going to read/write
    argv[2] : str
        unit, case insensitive.
        Including B, KB, MB, GB.
    argv[3] : str
        number of loops the test going to run on a fixed file size
    """

    if (len(sys.argv) != 3 and len(sys.argv) != 4) or sys.argv[2].lower() not in ['b', 'kb', 'mb', 'gb']: # parameters check
        print('Running default tests:')
        size_list = [1, 128, 256, 512, 1024, 2, 128, 256, 512]
        unit_list = ['kb', 'kb', 'kb', 'kb', 'kb', 'mb', 'mb', 'mb', 'mb']
        ws_result_list = list()
        rs_result_list = list()
        for i in range(9):
            print('Processing:' + str(size_list[i]) + str(unit_list[i]))
            test_result = test(FILE, size_list[i], unit_list[i])
            ws_result_list.append(test_result[0])
            rs_result_list.append(test_result[1])
        
        print(ws_result_list)
        print(rs_result_list)
        
        avg_ws_default = sum(ws_result_list) / float(len(ws_result_list))
        avg_rs_default = sum(rs_result_list) / float(len(rs_result_list))

        print("Average writing speed: %.2f Bytes / ms" % (avg_ws_default))
        print("Average reading speed: %.2f Bytes / ms" % (avg_rs_default))
        print('Note: You can also set the file size yourself, argument \'times\' is optional.')
        print('Usage: python [file_name].py [size] [unit] [times]')
        print('Example: python storage_test.py 10 kb 20')
    elif len(sys.argv) == 3:
        size = int(sys.argv[1])
        unit = sys.argv[2]

        test(FILE, size, unit)
    else: 
        times = int(sys.argv[3])
        size = int(sys.argv[1])
        unit = sys.argv[2]
        ws_result_list = list()
        rs_result_list = list()

        for i in range(times):
            test_result = test(FILE, size, unit)
            ws_result_list.append(test_result[0])
            rs_result_list.append(test_result[1])
        
        ws_mean = statistics.mean(ws_result_list)
        rs_mean = statistics.mean(rs_result_list)
        ws_stdev = statistics.stdev(ws_result_list)
        rs_stdev = statistics.stdev(rs_result_list)

        ws_ci_bound_var = 1.725 * ws_stdev / math.sqrt(20)
        rs_ci_bound_var = 1.725 * rs_stdev / math.sqrt(20)

        print("Mean of writing speed of : %.2f Bytes / ms" % (ws_mean))
        print("Mean of reading speed: %.2f Bytes / ms" % (rs_mean))
        print("Confidence interval of writing 20 times is: %.2f +- %.2f" %(ws_mean, ws_ci_bound_var))
        print("Confidence interval of reading 20 times is: %.2f +- %.2f" %(rs_mean, rs_ci_bound_var))
