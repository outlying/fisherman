import multiprocessing


def wrapper(queue, func, args, kwargs):
    result = func(*args, **kwargs)
    queue.put(result)


def run_with_timeout(func, timeout, *args, **kwargs):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=wrapper, args=(queue, func, args, kwargs))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()  # Forcefully terminate the process if it exceeds the timeout
        process.join()  # Wait for the process to terminate completely
        return None
    else:
        return queue.get()