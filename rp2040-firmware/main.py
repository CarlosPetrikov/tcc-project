from time import sleep

from configuration.environment import env
from utils.dht_sensor import DHTSensor
from utils.lcd_display import LCDDisplay
from utils.mqtt_client import MQTTClientWrapper
from utils.wifi_manager import WiFiManager


def main():
    """
    Função principal que inicializa Wi-Fi, MQTT, sensor DHT22 e display LCD,
    e mantém o loop de leitura, atualização do display e publicação no MQTT.
    """
    wifi = WiFiManager(env.wifi_ssid, env.wifi_password)
    wifi.connect()

    mqtt = MQTTClientWrapper(wifi.pool, env.mqtt_broker, client_id=env.mqtt_client_id)
    mqtt.connect()

    dht_sensor = DHTSensor(env.pin_dht22)
    lcd = LCDDisplay(env.pin_display_scl, env.pin_display_sda)

    while True:
        temperature, humidity = dht_sensor.read_all()
        lcd.update(temperature, humidity)

        if temperature is not None:
            mqtt.publish_float(env.topic_temperature, temperature)
        if humidity is not None:
            mqtt.publish_float(env.topic_humidity, humidity)

        sleep(2)


if __name__ == "__main__":
    main()
