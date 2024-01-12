import time


def countdown_timer(sec):
    while sec > 0:
        print(f"Time remaining: {sec} seconds.")
        time.sleep(1)
        sec -= 1
    print("Time is up!")

x = input("Enter the seconds you want to count down: ")
countdown_timer(int(x))
