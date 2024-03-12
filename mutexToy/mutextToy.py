import threading

# Create a Lock object
lock = threading.Lock()

def critical_section(id):
    with lock:
        # Critical section of code
        print(f"Thread {id} entering the critical section")
        # Simulate some work
        print(f"Thread {id} leaving the critical section")


if __name__ == '__main__':
    # Create multiple threads that access the critical section
    threads = [threading.Thread(target=critical_section, args=(i,)) for i in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
