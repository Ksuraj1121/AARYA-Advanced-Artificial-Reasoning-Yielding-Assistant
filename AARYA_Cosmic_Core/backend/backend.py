from PySide6.QtCore import QObject, Property, Signal, Slot, QTimer

from backend.system_monitor import get_system_info


class Backend(QObject):
    dataChanged = Signal()

    def __init__(self):
        super().__init__()

        self._cpu = 0
        self._ram = 0
        self._disk = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_system_info)
        self.timer.start(1000)  # Update every second

        self.update_system_info()

    @Slot()
    def update_system_info(self):
        info = get_system_info()

        self._cpu = info["cpu"]
        self._ram = info["ram"]
        self._disk = info["disk"]

        self.dataChanged.emit()

    @Property(float, notify=dataChanged)
    def cpu(self):
        return self._cpu

    @Property(float, notify=dataChanged)
    def ram(self):
        return self._ram

    @Property(float, notify=dataChanged)
    def disk(self):
        return self._disk