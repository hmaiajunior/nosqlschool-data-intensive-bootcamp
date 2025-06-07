"""

### TESTES:
# Variar, p/ confirmar até onde seu server aguenta em termos de requests:
# Qtde de Threads
# Tamanho da Key
# Tamanho do Value

"""
 


# pip install redis

import redis
import threading
import time
import random

host = 'redis-10141.c274.us-east-1-3.ec2.redns.redis-cloud.com'
port = '10141'
username = 'default'
password = 'YJLo0B4HfCZhnyeEYozeQs2MnjrU2bN8'

# Configurações do cluster Redis
redis_nodes = [
    {'host': host, 'port': port, },
    #{'host': 'localhost', 'port': 6380},
    #{'host': 'localhost', 'port': 6381}
]


# Conectar a um nó do cluster
def connect_redis(node, username, password):
    #return redis.Redis(host=node['host'], port=node['port'])
    return redis.Redis(
        host=node['host'],
        port=node['port'],
        decode_responses=True,
        username=username,
        password=password,
    )

# Função para executar carga no Redis
def load_test(client, thread_id, duration=60):
    start_time = time.time()
    while time.time() - start_time < duration:
        key = f"trest:{thread_id}:{random.randint(1, 100000000)}"
        #value = "X" * 1024  # 1KB de dados
        value = "X" * 50048
        try:
            client.set(key, value)
            client.get(key)
            client.delete(key)
        except Exception as e:
            print(f"Erro no thread {thread_id}: {e}")

# Iniciar múltiplas threads para carga
def start_load_test(threads=10, duration=60):
    clients = [connect_redis(random.choice(redis_nodes), username, password) for _ in range(threads)]
    threads_list = []

    print(f"Iniciando teste de carga com {threads} threads por {duration} segundos.")
    for i in range(threads):
        thread = threading.Thread(target=load_test, args=(clients[i], i, duration))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

    print("Teste de carga concluído.")

if __name__ == "__main__":
    start_load_test(threads=5, duration=120)


