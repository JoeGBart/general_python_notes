import time
from functools import wraps
from memory_profiler import memory_usage


def short_process_profile(fn):
    """Decorator to measure the execution time and peak memory usage
    of python function. Function is called twice. Once for time
    measurement, once for memory measurement.
    """

    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"\n{fn.__name__}({fn_kwargs_str})")

        # Measure time
        t = time.perf_counter()
        retval = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t
        print(f"Time   {elapsed:0.4}")

        # Measure memory
        mem, retval = memory_usage(
            (fn, args, kwargs),
            retval=True,
            max_usage=True,
            interval=1e-7,
            max_iterations=1,
        )

        print(f"Memory {mem}")
        return retval

    return inner


def long_process_profile(fn):
    """Decorator to measure the execution time and peak memory usage
    of python function. Function is called only once. The time
    measurement and peak memory measurements taken for a single
    function call.

    Given the memory measurement increases the time measurement.
    It is recommended this decorator is only used on long-running
    functions. E.g. batch db inserts.
    """

    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"\n{fn.__name__}({fn_kwargs_str})")

        # Measure time
        t = time.perf_counter()

        # Measure memory
        mem, retval = memory_usage(
            (fn, args, kwargs),
            retval=True,
            max_usage=True,
            interval=1e-7,
            max_iterations=1,
        )
        elapsed = time.perf_counter() - t
        print(f"Time   {elapsed:0.4}")

        print(f"Memory {mem}")
        return retval

    return inner
