from os import getenv
import board

class Environment:
    """
    Classe para armazenar variáveis de ambiente do projeto, como credenciais Wi-Fi,
    broker MQTT, client_id, tópicos para publicação do sensor DHT22 e pinos do display e sensor.
    """

    def __init__(self) -> None:
        # --- Wi-Fi ---
        self._CIRCUITPY_WIFI_SSID: str = getenv("CIRCUITPY_WIFI_SSID")
        self._CIRCUITPY_WIFI_PASSWORD: str = getenv("CIRCUITPY_WIFI_PASSWORD")

        # --- MQTT ---
        self._MQTT_BROKER: str = getenv("MQTT_BROKER")
        self._MQTT_CLIENT_ID: str = getenv("MQTT_CLIENT_ID", "rpi_pico_w_client")

        # --- Tópicos DHT22 ---
        self._TOPIC_TEMPERATURE: str = getenv("MQTT_TOPIC_TEMPERATURE", "dht22/sensor/temperatura")
        self._TOPIC_HUMIDITY: str = getenv("MQTT_TOPIC_HUMIDITY", "dht22/sensor/umidade")

        # --- Pinos ---
        # Sensor DHT22
        self._PIN_DHT22: str = getenv("PIN_DHT22", "GP2")

        # Display I2C
        self._PIN_DISPLAY_SCL: str = getenv("PIN_DISPLAY_SCL", "GP1")
        self._PIN_DISPLAY_SDA: str = getenv("PIN_DISPLAY_SDA", "GP0")

        # Push Button
        self._PIN_PUSH_BUTTON: str = getenv("PIN_PUSH_BUTTON", "GP16")

    # --- Wi-Fi ---
    @property
    def wifi_ssid(self) -> str:
        """Retorna o SSID da rede Wi-Fi."""
        return self._CIRCUITPY_WIFI_SSID

    @property
    def wifi_password(self) -> str:
        """Retorna a senha da rede Wi-Fi."""
        return self._CIRCUITPY_WIFI_PASSWORD

    # --- MQTT ---
    @property
    def mqtt_broker(self) -> str:
        """Retorna o endereço do broker MQTT."""
        return self._MQTT_BROKER

    @property
    def mqtt_client_id(self) -> str:
        """Retorna o client_id do cliente MQTT."""
        return self._MQTT_CLIENT_ID

    # --- Tópicos DHT22 ---
    @property
    def topic_temperature(self) -> str:
        """Retorna o tópico MQTT para publicar a temperatura do DHT22."""
        return self._TOPIC_TEMPERATURE

    @property
    def topic_humidity(self) -> str:
        """Retorna o tópico MQTT para publicar a umidade do DHT22."""
        return self._TOPIC_HUMIDITY

    # --- Pinos ---
    @property
    def pin_dht22(self) -> str:
        """Retorna o pino digital do sensor DHT22."""
        return getattr(board, self._PIN_DHT22)

    @property
    def pin_display_scl(self) -> str:
        """Retorna o pino SCL do display I2C."""
        return getattr(board, self._PIN_DISPLAY_SCL)

    @property
    def pin_display_sda(self) -> str:
        """Retorna o pino SDA do display I2C."""
        return getattr(board, self._PIN_DISPLAY_SDA)

    @property
    def pin_push_button(self) -> str:
        """Retorna o pino SDA do display I2C."""
        return getattr(board, self._PIN_PUSH_BUTTON)

env = Environment()
