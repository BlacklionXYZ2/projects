import threading, time
from sys import stdout as console

threads = {}

task_len = 10
time_taken = 0

def progress_bar(t = task_len):
    for _ in range(t):
        out = '\r' + ('. ' * (_ + 1))
        console.flush()
        console.write(out)
        time.sleep(1)

def task():
    print('Task starting:')
    time.sleep(11)
    print('\nTask completed')

threads['1'] = threading.Thread(target = task)
threads['2'] = threading.Thread(target = progress_bar)

for x in threads:
    threads[x].start()