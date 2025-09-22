from configuration.environment import env
from utils.wifi_manager import WiFiManager
def main():
    """

    ...

    """

    WiFiManager(env.wifi_ssid, env.wifi_password).connect()

