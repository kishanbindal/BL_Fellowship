import time

def stopWatch():
    start = input("Would you Like to start? (type 'Start')\n")
    if start[0].upper() == 'S':
        start_time = time.time()
    stop = input("Press Stop? (Enter 'Stop')\n")
    if stop[0].upper() == 'S':
        stop_time = time.time()
    print(f"Time ====> {stop_time - start_time}")
    return stop_time-start_time

stopWatch()