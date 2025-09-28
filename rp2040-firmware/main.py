from time import sleep

from configuration.environment import env
from utils.dht_sensor import DHTSensor
from utils.lcd_display import LCDDisplay
from utils.mqtt_client import MQTTClientWrapper
from utils.wifi_manager import WiFiManager
from utils.input_button import PushButton

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
    button = PushButton(env.pin_push_button, pull="UP")
    lcd.turn_off_backlight()

    while True:
        try:
            temperature, humidity = dht_sensor.read_all()
            print(temperature, humidity)
            lcd.update(temperature, humidity)

            if button.is_pressed():
                lcd.turn_on_backlight()
                lcd.update(temperature, humidity)
                sleep(5)
                lcd.turn_off_backlight()

            if temperature is not None:
                mqtt.publish_float(env.topic_temperature, temperature)
            if humidity is not None:
                mqtt.publish_float(env.topic_humidity, humidity)
        except Exception as e:
            print(e)
        finally:
            sleep(2)


if __name__ == "__main__":
    main()
