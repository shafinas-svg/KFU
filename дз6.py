import time
import random
import threading
import multiprocessing
import asyncio


def print_time(name, start_time):
    end_time = time.time()
    print(name, round(end_time - start_time, 2), "секунд")
    print()


def process_order(order_id):
    time.sleep(random.randint(1, 2))

    result = 0
    for i in range(100000, 500000):
        result += i ** 2 % 100

    print("Заказ", order_id, "готов")
    return result


def run_orders_sync():
    print("Threading sync")

    start_time = time.time()

    for order_id in range(1, 6):
        process_order(order_id)

    print_time("Время:", start_time)


def run_orders_threading():
    print("Threading")

    start_time = time.time()

    threads = []

    for order_id in range(1, 6):
        thread = threading.Thread(target=process_order, args=(order_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print_time("Время:", start_time)


def heavy_calculation(n):
    result = 0

    for i in range(1, n):
        result += (i * i) % 123
        result += i ** 2 % 456

    return result


def run_heavy_sync():
    print("Multiprocessing sync")

    start_time = time.time()

    numbers = [
        5000000,
        5000000,
        5000000,
        5000000
    ]

    results = []

    for n in numbers:
        result = heavy_calculation(n)
        results.append(result)

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


def run_heavy_multiprocessing():
    print("Multiprocessing")

    start_time = time.time()

    numbers = [
        5000000,
        5000000,
        5000000,
        5000000
    ]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_calculation, numbers)

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


async def service_request(user_id):
    await asyncio.sleep(random.randint(1, 2))

    result = 0
    for i in range(300000, 700000):
        if i % 2 == 0:
            result += i % 100

    print("Пользователь", user_id, "готов")
    return result


async def run_async_tasks():
    print("Async")

    start_time = time.time()

    tasks = []

    for user_id in range(1, 11):
        task = service_request(user_id)
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


def universal_task(task_id):
    time.sleep(1)

    result = 0
    for i in range(500000):
        result += (i * task_id) % 100

    time.sleep(1)

    result = result + task_id

    print("Задача", task_id, "готова")
    return result


def run_universal_sync():
    print("Смешанный sync")

    start_time = time.time()

    results = []

    for task_id in range(1, 6):
        result = universal_task(task_id)
        results.append(result)

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


def run_universal_threading():
    print("Смешанный threading")

    start_time = time.time()

    threads = []
    results = []

    def wrapper(task_id):
        result = universal_task(task_id)
        results.append(result)

    for task_id in range(1, 6):
        thread = threading.Thread(target=wrapper, args=(task_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


def run_universal_multiprocessing():
    print("Смешанный multiprocessing")

    start_time = time.time()

    task_ids = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(universal_task, task_ids)

    print("Результаты получены:", len(results))
    print_time("Время:", start_time)


if __name__ == "__main__":

    run_orders_sync()
    run_orders_threading()

    run_heavy_sync()
    run_heavy_multiprocessing()

    asyncio.run(run_async_tasks())

    run_universal_sync()
    run_universal_threading()
    run_universal_multiprocessing()

    print("Готово")