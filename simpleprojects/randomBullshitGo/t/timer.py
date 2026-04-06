import time
import datetime

def time_callback(timer):
    """
    A function to be called every 10 seconds.  This is a placeholder
    for the core logic of your program.  You'll replace this with your
    actual time update or data processing.
    """
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Format the time

    print(f"Time: {current_time}")

    time.sleep(1)  # Pause for 10 seconds


def main():
    """
    The main function to start the timer.
    """
    timer = None

    while True:
        time_callback(timer)  # Call the callback function

if __name__ == "__main__":
    main()