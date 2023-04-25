import multiprocessing
from multiprocessing import Pool, cpu_count
import time

def factorize(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize_async(numbers):
    with Pool(cpu_count()) as p:
        result = p.map_async(factorize, numbers)
        while not result.ready():
            time.sleep(0.1)
        return result.get()

if __name__ == "__main__":
    multiprocessing.freeze_support()

    a, b, c, d = factorize_async([128, 255, 99999, 10651060])
    print(a)
    print(b)
    print(c)
    print(d)


    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
