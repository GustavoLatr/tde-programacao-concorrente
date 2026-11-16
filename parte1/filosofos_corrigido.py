import threading
import time

numero_filosofos = 5
estados = ["pensando"] * numero_filosofos
garfos = [threading.Lock() for _ in range(numero_filosofos)]

lock_print = threading.Lock()
def mudar_estado(indice_filosofo, novo_estado):
    with lock_print:
        estados[indice_filosofo] = novo_estado
        print(f"Fílosofo {indice_filosofo}: está {novo_estado} Mesa: {estados}")

def filosofo_corrigido(p):
    garfo_esq = p
    garfo_dir = (p + 1) % numero_filosofos
    primeiro = min(garfo_esq, garfo_dir)
    segundo = max(garfo_esq, garfo_dir)

    while True:
        mudar_estado(p, "pensando")
        time.sleep(0.2)

        mudar_estado(p, "com fome")
        garfos[primeiro].acquire()
        time.sleep(0.2)
        garfos[segundo].acquire()
        mudar_estado(p, "comendo")
        time.sleep(0.2)
        garfos[primeiro].release()
        garfos[segundo].release()
if __name__ == "__main__":
    threads = []
    for p in range(numero_filosofos):
        t = threading.Thread(target=filosofo_corrigido, args=(p,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()