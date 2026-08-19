import time

t = input("Enter time (in seconds): ")

if t.isdigit():
    t = int(t)
else:
    print("Invalid input!")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("Time's up!")
