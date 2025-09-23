import threading
import time

n = [3,2,1]
#without multithreading
def wait_and_print(i):
    time.sleep(i)
    print(f"task runs in {i}")


threads=[]
for i in n:
    t=threading.Thread(target=wait_and_print, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    print('i')
    t.join()


for i in n:
    wait_and_print(i)

