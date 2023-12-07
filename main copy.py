from multiprocessing import Process, cpu_count
from time import time


cpus_count = cpu_count()


def factorize(number):
    new_lst = []
    for i in range(1, number + 1):
        if (number % (i)) == 0:
            new_lst.append(i)
    print(new_lst)
    return new_lst


if __name__ == "__main__":
    start_exec = time()
    proccess = []
    data = [128, 255, 99999, 10651060]
    for i in data:
        p = Process(target=factorize, args=(i,))
        p.start()

    end_exec = time()
    print(f"Execution time is {end_exec - start_exec}")
