import threading
import time

Threads = 8
Movimentos = 10000
count = 0
sem = threading.Semaphore(1)

def task_sem_semaforo():
    global count
    for _ in range(Movimentos):
        temp = count
        time.sleep(0)
        temp = temp + 1
        count = temp

def task_com_semaforo():
    global count
    for _ in range(Movimentos):
        sem.acquire()
        try:
            temp = count
            temp = temp + 1
            count = temp
        finally:
            sem.release()

if __name__ == "__main__":
    esperado = Threads * Movimentos
    count = 0
    lista_threads = []
    inicio = time.perf_counter()


    for _ in range(Threads):
        t = threading.Thread(target=task_sem_semaforo)
        lista_threads.append(t)
        t.start()

    for t in lista_threads:
        t.join()

    fim = time.perf_counter()
    print(f"SEM SEMAFORO -> Esperado: {esperado} | Obtido: {count} | Tempo: {fim - inicio:.4f}s")
    count = 0
    lista_threads = []
    inicio = time.perf_counter()

    for _ in range(Threads):
        t = threading.Thread(target=task_com_semaforo)
        lista_threads.append(t)
        t.start()

    for t in lista_threads:
        t.join()

    fim = time.perf_counter()
    print(f"COM SEMAFORO -> Esperado: {esperado} | Obtido: {count} | Tempo: {fim - inicio:.4f}s")

