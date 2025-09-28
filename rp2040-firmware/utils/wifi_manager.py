import ipaddress

import wifi
from socketpool import SocketPool


class WiFiManager:
    """
    Gerencia a conexão Wi-Fi em dispositivos CircuitPython.

    Esta classe encapsula a lógica de conexão a uma rede Wi-Fi, acesso ao
    socket pool e utilitários como leitura de IP, MAC address e teste de ping.

    Parameters
    ----------
    ssid : str, optional
        Nome da rede Wi-Fi (SSID). Deve estar definido no `settings.toml`
        como `CIRCUITPY_WIFI_SSID` caso não seja passado no construtor.
    password : str, optional
        Senha da rede Wi-Fi. Deve estar definida no `settings.toml`
        como `CIRCUITPY_WIFI_PASSWORD` caso não seja passada no construtor.

    Attributes
    ----------
    ssid : str
        SSID configurado para conexão.
    password : str
        Senha configurada para conexão.
    pool : socketpool.SocketPool
        Pool de sockets associado ao rádio Wi-Fi.
    """

    def __init__(self, ssid: str = None, password: str = None) -> None:
        """
        Inicializa o gerenciador Wi-Fi com credenciais fornecidas
        ou lidas do `settings.toml`.

        Raises
        ------
        RuntimeError
            Se `ssid` ou `password` não forem fornecidos.
        """
        self.ssid: str = ssid
        self.password: str = password
        self.pool: SocketPool = None

        if None in [self.ssid, self.password]:
            raise RuntimeError("'CIRCUITPY_WIFI_SSID' e 'CIRCUITPY_WIFI_PASSWORD' não definidos no settings.toml")

    def connect(self) -> None:
        """
        Conecta ao Wi-Fi usando as credenciais fornecidas.

        Returns
        -------
        None

        Raises
        ------
        ConnectionError
            Se a conexão falhar.
        TypeError
            Se a rede não for encontrada ou as credenciais estiverem incorretas.
        """
        print("\nConectando no Wi-Fi...")
        try:
            wifi.radio.connect(self.ssid, self.password)
        except TypeError:
            print(f"Rede {self.ssid} indisponível. Verifique seu settings.toml")
            raise

        self.pool = SocketPool(wifi.radio)
        print(f"Conectado na rede {self.ssid}")

    def get_mac_address(self) -> str:
        """
        Retorna o endereço MAC do dispositivo.

        Returns
        -------
        str
            Endereço MAC no formato de lista de hexadecimais.
        """
        return str([hex(i) for i in wifi.radio.mac_address])

    def get_ip_address(self) -> str:
        """
        Retorna o endereço IPv4 atribuído ao dispositivo.

        Returns
        -------
        str
            Endereço IPv4 em formato de string.
        """
        return wifi.radio.ipv4_address

    def ping(self, host: str = "8.8.4.4") -> float | None:
        """
        Envia um ping para o host informado.

        Parameters
        ----------
        host : str, default="8.8.4.4"
            Endereço IP ou hostname a ser testado.

        Returns
        -------
        float or None
            Tempo de resposta em milissegundos, ou `None` se não houver resposta.

        Raises
        ------
        Exception
            Se ocorrer falha no envio do ping.
        """

        ipv4 = ipaddress.ip_address(host)
        try:
            response = wifi.radio.ping(ipv4)
            if response is None:
                return None
            return response * 1000
        except Exception as e:
            print(f"Ping falhou: {e}")
            return None
