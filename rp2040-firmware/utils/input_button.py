import digitalio
import board
from time import monotonic

class PushButton:
    """
    Classe para gerenciar um botão conectado a um pino do Pico.
    Suporta pull-up ou pull-down interno.
    """

    def __init__(self, pin, pull="UP"):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.INPUT
        if pull.upper() == "UP":
            self.pin.pull = digitalio.Pull.UP
            self.active_state = False
        elif pull.upper() == "DOWN":
            self.pin.pull = digitalio.Pull.DOWN
            self.active_state = True
        else:
            raise ValueError("pull deve ser 'UP' ou 'DOWN'")

        # Para detecção de debounce
        self._last_state = self.pin.value
        self._last_change_time = monotonic()
        self._debounce_time = 0.05  # 50ms

    def is_pressed(self):
        """Retorna True se o botão estiver pressionado (considerando debounce)."""
        current = self.pin.value
        now = monotonic()
        if current != self._last_state:
            self._last_change_time = now
            self._last_state = current

        if (now - self._last_change_time) > self._debounce_time:
            return current == self.active_state
        return False
