from abc import ABC, abstractmethod
import sys

from PyQt6.QtWidgets import QApplication, QMessageBox


class Car(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class SportCar(Car):

    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if self.engine_running:
            return False

        print("Engine started")
        self.engine_running = True
        return True

    def stop_engine(self):
        if not self.engine_running:
            return False

        print("Engine stopped")
        self.engine_running = False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)

    car = SportCar()

    if car.start_engine():
        QMessageBox.information(
            None,
            "Success",
            "Engine started successfully."
        )
    else:
        QMessageBox.warning(
            None,
            "Warning",
            "Engine is already running."
        )

    sys.exit(app.exec())