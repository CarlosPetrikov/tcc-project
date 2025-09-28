import busio
from i2c_pcf8574_interface import I2CPCF8574Interface
from lcd import LCD


class LCDDisplay:
    """
    Classe para gerenciar um display LCD via I2C.

    Esta classe encapsula a inicialização do display, criação de caracteres
    personalizados e atualização das informações de temperatura e umidade.
    """

    def __init__(self, scl, sda, i2c_address: int = 0x27, num_rows: int = 2, num_cols: int = 16) -> None:
        """
        Inicializa o LCD via I2C.

        Parameters
        ----------
        scl : busio pin
            Pino SCL da interface I2C.c
        sda : busio pinc
            Pino SDA da interface I2C.
        i2c_address : int, default=0x27
            Endereço I2C do módulo LCD.
        num_rows : int, default=2
            Número de linhas do display.
        num_cols : int, default=16
            Número de colunas do display.
        """
        i2c = busio.I2C(scl, sda)
        self.lcd = LCD(I2CPCF8574Interface(i2c, i2c_address), num_rows=num_rows, num_cols=num_cols)
        self._create_custom_chars()
        self.clear()
        self._initialize_display_template()

    def _create_custom_chars(self) -> None:
        """
        Cria caracteres personalizados no LCD.
        """
        celsius = (0x00, 0x07, 0x05, 0x07, 0x00, 0x00, 0x00, 0x00)
        self.lcd.create_char(0, celsius)
        self.SYMBOLS = {"celsius": 0}

    def clear(self) -> None:
        """Limpa o display."""
        self.lcd.clear()

    def _initialize_display_template(self) -> None:
        """Inicializa a tela com os textos fixos."""
        self.lcd.set_cursor_pos(0, 0)
        self.lcd.print("Temp:    00.0")
        self.lcd.write(self.SYMBOLS["celsius"])
        self.lcd.print("C")
        self.lcd.set_cursor_pos(1, 0)
        self.lcd.print("Umidade: 00.0 %")

    def update_temperature(self, temperature: float | None) -> None:
        """
        Atualiza o valor da temperatura no display.

        Parameters
        ----------
        temperature : float | None
            Valor da temperatura em Celsius. Ignora se None.
        """
        if temperature is not None:
            self.lcd.set_cursor_pos(0, 9)
            self.lcd.print(f"{temperature:>4.1f}")

    def update_humidity(self, humidity: float | None) -> None:
        """
        Atualiza o valor da umidade no display.

        Parameters
        ----------
        humidity : float | None
            Valor da umidade em %. Ignora se None.
        """
        if humidity is not None:
            self.lcd.set_cursor_pos(1, 9)
            self.lcd.print(f"{humidity:>4.1f}")

    def update(self, temperature: float | None, humidity: float | None) -> None:
        """
        Atualiza temperatura e umidade ao mesmo tempo.

        Parameters
        ----------
        temperature : float | None
        humidity : float | None
        """
        self.update_temperature(temperature)
        self.update_humidity(humidity)

    def turn_on_backlight(self):
        self.lcd.set_backlight(True)

    def turn_off_backlight(self):
        self.lcd.set_backlight(False)