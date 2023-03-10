import sys
from window.register_window import RegisterWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    try:
        
        app = QApplication([])
        window = RegisterWindow()
        window.show()
        app.exec()

        
    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    finally:
        sys.exit()