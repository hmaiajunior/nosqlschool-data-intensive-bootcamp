# nosqlschool-data-intensive-bootcamp
Imersao - data intensive bootcamp - redis, kafka, aws, grafana

Endereço grafana: http://localhost:3000

Endereço kafka-ui: http://localhost:8087

Endereço prometheus: http://localhost:9090/

Endereço métricas: http://localhost:9308/metrics


O container node-exporter bate no kafka e consome as métricas expondo na URL de métricas. O prometheus faz o scrapy de acordo com as definições no arquivo prometheus.yml. Daí o grafana consome as métricas batendo no endereço do prometheus.
