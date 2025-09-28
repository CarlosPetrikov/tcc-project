from adafruit_dht import DHT22


class DHTSensor:
    """
    Classe para gerenciar o sensor DHT22.

    Esta classe encapsula a leitura de temperatura e umidade, lidando com
    possíveis exceções durante a leitura do sensor.
    """

    def __init__(self, pin) -> None:
        """
        Inicializa o sensor DHT22.

        Parameters
        ----------
        pin : microcontroller.Pin
            Pino digital ao qual o DHT22 está conectado.
        """
        self._dht = DHT22(pin)

    def read_temperature(self) -> float | None:
        """
        Lê a temperatura em Celsius.

        Returns
        -------
        float | None
            Temperatura em Celsius, ou None se a leitura falhar.
        """
        try:
            return self._dht.temperature
        except RuntimeError as e:
            print(f"Erro ao ler temperatura: {e}")
            return None

    def read_humidity(self) -> float | None:
        """
        Lê a umidade relativa.

        Returns
        -------
        float | None
            Umidade em %, ou None se a leitura falhar.
        """
        try:
            return self._dht.humidity
        except RuntimeError as e:
            print(f"Erro ao ler umidade: {e}")
            return None

    def read_all(self) -> tuple[float | None, float | None]:
        """
        Lê temperatura e umidade ao mesmo tempo.

        Returns
        -------
        tuple[float | None, float | None]
            (temperatura, umidade)
        """
        return self.read_temperature(), self.read_humidity()
