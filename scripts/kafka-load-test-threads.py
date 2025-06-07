"""
pip install confluent_kafka
"""


import threading
import time
import random
import string
from confluent_kafka import Producer
import json



# Configurações de conexão com a Confluent Cloud
producer_config = {
    'bootstrap.servers': 'pkc-p11xm.us-east-1.aws.confluent.cloud:9092', 
#    'sasl.username': 'N5UA7PWEBFGHGKFJ',
#    'sasl.password': 'YvfeK8x4CKs3Nm8CyTHdG/tAJyATaAFSLifFD0vOewkL27NS4kxWnqEB39DUUjAH',
    'sasl.username': '4KEE6J25VHWFIT6M',
    'sasl.password': 'XYYP1QXSZmlwuDVzYDKPu2QnvP5AcC5jCQqn6v8kJw0k5GePLh2oZYId27JB4n8B',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN'
}


# Nome do tópico a ser utilizado
KAFKA_TOPIC = 'topic_bootcamp_nosql'
#KAFKA_TOPIC = 'topic_bc_new_2'
#KAFKA_TOPIC = 'topic_bc_0'

# Define o número de mensagens que cada thread irá produzir (teste de carga)
MESSAGES_PER_THREAD = 200000

# Define a quantidade de threads simultâneas
#NUM_THREADS = 5
NUM_THREADS = 10

def delivery_report(err, msg):
    """
    Callback que é chamada quando a entrega de uma mensagem é confirmada ou falha.
    """
    if err is not None:
        print(f'Falha ao enviar mensagem: {err}')
    else:
        #print(f'MSG entregue: tópico {msg.topic()} - particao {msg.partition()}')
        pass

def generate_random_string(length=10):
    """
    Gera uma string aleatória para simular um payload.
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def produce_messages(producer_id, num_messages):
    """
    Função que irá produzir 'num_messages' mensagens no tópico Kafka,
    usando um determinado 'producer_id' para identificação.
    """
    # Instancia o Producer
    p = Producer(producer_config)

    for i in range(num_messages):
        payload = generate_random_string(50)
        
        #payload2 = {
        #    'Nome' : 'Nome1',
        #    'Idade' : '50'
        #}
        #payload2 = json.dumps(payload2)
        
        # Produz mensagem de forma assíncrona
        p.produce(
            topic=KAFKA_TOPIC,
            key=f'thread-d1-{producer_id}-{i}',
            value=payload,
            callback=delivery_report  # callback opcional
        )

        # Opcional: envia mensagens em lote para evitar que o buffer fique cheio
        # ou que o callback não seja chamado em tempo hábil.
        p.poll(0)
    
    # Força o envio de todas as mensagens que estão em buffer
    p.flush()
    print(f'Thread {producer_id} finalizada. Total de mensagens enviadas: {num_messages}')

def main():
    threads = []

    start_time = time.time()

    for i in range(NUM_THREADS):
        t = threading.Thread(target=produce_messages, args=(i, MESSAGES_PER_THREAD))
        t.start()
        threads.append(t)

    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()

    end_time = time.time()
    total_time = end_time - start_time
    total_messages = NUM_THREADS * MESSAGES_PER_THREAD
    print(f'\nEnvio concluído. Total de {total_messages} mensagens em {total_time:.2f} segundos.')
    print(f'Taxa aproximada: {total_messages/total_time:.2f} mensagens/segundo')

if __name__ == '__main__':
    main()
