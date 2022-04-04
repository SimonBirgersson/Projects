"""
Handy functions for keeping time, or sleeping the function or such.
"""
import time


# Define timer function
def timer(func):
    """
    Take the time an function needs to finish, use as a wrapper!
    """
    # define wrapper function to use for other functions
    def wrapper(*args, **kwargs):

        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()

        print(f"function {func.__name__!r} finished after {t2-t1:.2f}s. \n")
        return result

    return wrapper


# define the countdown func.
def countdown(t: int):
    """
    function that counts down from t to 0 seconds and puts the script to sleep meanwhile. useful for scraping websites for instance, as it can prevent API query limits.
    """
    while t:
        mins, secs = divmod(t, 60)
        length = f"{mins:02d}:{secs:02d}"
        print(length, end="\r")
        time.sleep(1)
        t -= 1
    print("Done!")
