# SMAC-IoT - TCC Engenharia da Computação UNINTER

Bem-vindo ao repositório do **SMAC-IoT**, um projeto desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) da disciplina de Engenharia da Computação da UNINTER.

O objetivo deste projeto é implementar uma **prova de conceito (PoC)** de monitoramento ambiental usando sensores IoT, demonstrando a viabilidade da ideia e facilitando a replicação em outros ambientes de teste.

> ⚠️ Este projeto é destinado apenas para **fins de teste em ambiente local**. Para simplificar a replicação, não há autenticação ou autorização nos serviços, portanto **não deve ser usado em produção**.

---

## Estrutura do Repositório

```
.
├── docs
│   ├── img
│   └── mmd
│       ├── class_diagram.mmd          # Diagrama de classes do código
│       ├── code_flow.mmd               # Fluxo principal do código
│       ├── communication_flow.mmd      # Fluxo de comunicação entre Pi Pico e containers
│       └── entity_relationship.mmd     # Modelo do bucket InfluxDB
├── rp2040-firmware                      # Código para o Raspberry Pi Pico W
├── rpi5-iac                             # Configuração do servidor via Docker Compose
└── tmp                                  # Pasta temporária para sincronização no Pi Pico W
```

* **docs/mmd**: diagramas Mermaid do projeto, incluindo classes, fluxo de código, comunicação e modelo do InfluxDB.
* **rp2040-firmware**: firmware do Pi Pico W, com classes de sensor, display e MQTT.
* **rpi5-iac**: configurações de containers Docker para o servidor (Mosquitto, Node-RED, InfluxDB e Grafana).
* **tmp**: pasta temporária para copiar os arquivos do projeto para o Pi Pico.

---

## Configuração do Servidor IoT (Raspberry Pi 5)

O servidor é configurado via **Docker Compose** e sobe os seguintes serviços:

* **Mosquitto**: broker MQTT para receber os dados do sensor DHT22.
* **Node-RED**: consome os tópicos MQTT e envia os dados para o InfluxDB.
* **InfluxDB**: banco de dados de séries temporais, com bucket `smac-iot`.
* **Grafana**: painel de visualização dos dados armazenados no InfluxDB.

> 💡 É recomendado instalar o **Portainer** para monitorar os containers de forma visual.

### Acessando o Grafana

Após subir os containers:

```
http://<IP_DO_RPI5>:3000
```

* Usuário anônimo com permissão de **Admin**.
* Dashboards configurados para visualizar os dados de temperatura e umidade do bucket `smac-iot`.

---

## Configuração do Raspberry Pi Pico W

1. **Instalar CircuitPython** no Pi Pico W.
2. **Remover** o arquivo `code.py` padrão.
3. **Sincronizar o código** usando os comandos `taskipy` do Poetry:

```bash
poetry run taskipy sync        # copia os arquivos para o Pi Pico
poetry run taskipy pico_output # abre o console serial
poetry run taskipy format      # formata o código
poetry run taskipy minify      # opcional: minifica o código
```

4. Certifique-se de copiar todos os arquivos necessários:

   * `configuration/environment.py`
   * `main.py`
   * `utils/` (classes auxiliares)
   * `lib/` (dependências CircuitPython como `adafruit_dht.mpy` e `adafruit_minimqtt`)

O Pi Pico irá:

* Conectar ao Wi-Fi.
* Ler os dados do sensor DHT22 (temperatura e umidade).
* Atualizar o display LCD 16x2 via I2C.
* Publicar os valores nos tópicos MQTT (`temperature` e `humidity`).

---

## Diagramas

* **class\_diagram.mmd** → Classes do código (`WiFiManager`, `MQTTClientWrapper`, `DHTSensor`, `LCDDisplay`) e suas relações.
* **code\_flow\.mmd** → Fluxo principal do código (`main.py`) com loop de leitura e publicação.
* **communication\_flow\.mmd** → Sequência de mensagens entre Pi Pico, Mosquitto, Node-RED, InfluxDB e Grafana.
* **entity\_relationship.mmd** → Modelo do bucket `smac-iot` no InfluxDB.
* **Diagrama elétrico** → será adicionado futuramente, mostrando a conexão dos pinos do sensor e display.

---