import multiprocessing
import time


def adder(v):
    return sum([i for i in range(v)])

def find_sums_slow(numbers):
    for v in numbers:
        adder(v)

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(adder, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums_slow(numbers)
    print(time.time() - start_time)
    start_time = time.time()
    find_sums(numbers)
    dur = time.time() - start_time
    print(dur)
