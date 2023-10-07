import functools

from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            total_time = 0
            counter = 0
            while counter != num:
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                spent_time = end_time - start_time
                total_time += spent_time
                counter += 1
                print(f'Прогон {counter} время выполнения прогона: {spent_time}')
            print(f'Среднее время всех прогонов: {total_time / num}')
        return inner
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
