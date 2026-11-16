import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def tarefa(nome):
    print(f"{nome}:Tentando pegar LOCK_A...")
    with lock_a:
        print(f"{nome}:Pegou LOCK_A")
        time.sleep(0.1)
        print(f"{nome}: Tentando pegar LOCK_B...")
        with lock_b:
            print(f"{nome}:Pegou LOCK_B e terminou.")

t1 = threading.Thread(target=tarefa, args=("Thread-1",))
t2 = threading.Thread(target=tarefa, args=("Thread-2",))

t1.start()
t2.start()
t1.join()
t2.join()
print("Fim! Ninguém travou.")