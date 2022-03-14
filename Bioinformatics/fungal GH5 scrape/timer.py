# timer
# import the time module
import time


# define the countdown func.
def countdown(t: int):
    """function that counts down from t to 0 seconds."""
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Done!")
