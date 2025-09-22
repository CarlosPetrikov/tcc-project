from os import getenv

class Environment:
    def __init__(self):
        self._CIRCUITPY_WIFI_SSID: str = getenv("CIRCUITPY_WIFI_SSID")
        self._CIRCUITPY_WIFI_PASSWORD: str = getenv("CIRCUITPY_WIFI_PASSWORD")

    @property
    def wifi_ssid(self) -> str:
        return self._CIRCUITPY_WIFI_SSID

    @property
    def wifi_password(self) -> str:
        return self._CIRCUITPY_WIFI_PASSWORD


env = Environment()
