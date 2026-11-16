import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    print(": Tentando adiquirir LOCK_A...")
    with lock_a:
        print("T1: Adiquiriu lock_a.")
        time.sleep(0.1)  # força a troca  de contexto para causar o deadlock
        print(" T1: Tentando adiquirir LOCK_B...")
        with lock_b:
            print("T2: Tentando adiquirir LOCK_B.")

def thread_2():
    print(": Tentando adiquirir LOCK_B...")
    with lock_b:
        time.sleep(0.1)
        print("T2: Tentando adiquirir LOCK_A...")
        with lock_a:
            print("T2: Adiquiriu LOCK_A e concluiu.")

t1 = threading.Thread(target=thread_1, name="Thread-1")
t2 = threading.Thread(target=thread_2, name="Thread-2")

t1.start()
t2.start()

