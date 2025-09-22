from adafruit_minimqtt.adafruit_minimqtt import MQTT


class MQTTClientWrapper:
    """
    Classe para gerenciar conexão com um broker MQTT e publicar mensagens.

    Esta classe encapsula a lógica de conexão MQTT utilizando um SocketPool
    existente (por exemplo, de um WiFiManager) e fornece métodos para
    publicar valores float em tópicos específicos.

    Parameters
    ----------
    pool : SocketPool
        SocketPool já inicializado, geralmente obtido de um WiFiManager.
    broker : str
        Endereço do broker MQTT.
    port : int, default=1883
        Porta do broker MQTT.
    username : str | None, optional
        Nome de usuário para autenticação MQTT.
    password : str | None, optional
        Senha para autenticação MQTT.
    client_id : str | None, optional
        Identificador único do cliente MQTT.
    """

    def __init__(
        self,
        pool,
        broker: str,
        port: int = 1883,
        username: str | None = None,
        password: str | None = None,
        client_id: str | None = None,
    ) -> None:
        self.pool = pool
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password
        self.client_id = client_id

        self.mqtt_client = MQTT(
            broker=self.broker,
            port=self.port,
            socket_pool=self.pool,
            username=self.username,
            password=self.password,
            client_id=self.client_id,
        )
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_publish = self.on_publish

    def connect(self) -> None:
        """
        Conecta ao broker MQTT utilizando as credenciais e pool fornecidos.

        Raises
        ------
        RuntimeError
            Se a conexão falhar.
        """
        print(f"Conectando ao broker {self.broker}...")
        self.mqtt_client.connect()
        print("Conectado!")

    def publish_float(self, topic: str, value: float) -> None:
        """
        Publica um valor float em um tópico MQTT específico.

        Parameters
        ----------
        topic : str
            Tópico MQTT onde a mensagem será publicada.
        value : float
            Valor numérico a ser enviado. Será convertido em string com duas casas decimais.
        """
        payload = f"{value:.2f}"
        self.mqtt_client.publish(topic, payload)
        print(f"Publicado {payload} em {topic}")

    # Callbacks
    def on_connect(self, client: MQTT, userdata: object | None, flags: dict, rc: int) -> None:
        """Chamado quando a conexão MQTT é estabelecida com sucesso."""
        print("MQTT conectado!")

    def on_disconnect(self, client: MQTT, userdata: object | None, rc: int) -> None:
        """Chamado quando a conexão MQTT é perdida."""
        print("MQTT desconectado!")

    def on_publish(self, client: MQTT, topic: str, pid: int) -> None:
        """Chamado quando uma mensagem é publicada com sucesso."""
        print(f"Mensagem publicada em {topic} com pid {pid}")
