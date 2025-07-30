class Package:
    def __init__(self, mass, width, height, length):
        self.mass = self._set_measurement_validation('mass', mass)
        self.width = self._set_measurement_validation('width', width)
        self.height = self._set_measurement_validation('height', height)
        self.length = self._set_measurement_validation('length', length)
        self.volume = self._get_volume()
        self.bulky = self._is_bulky()
        self.heavy = self._is_heavy()

    def _set_measurement_validation(self, name, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError(f"{name} must be either a floating point or integer primitive data type. Not {type(value)}")
        if round(value, 2) <= 0.00:
            raise ValueError(f"{name} cannot be a negative value. Value received {value}")
        return value

    def _is_bulky(self) -> bool:
        return self.volume > 1_000_000

    def _is_heavy(self) -> bool:
        return self.mass > 20

    def _get_volume(self) -> None:
        return self.width * self.height * self.length
