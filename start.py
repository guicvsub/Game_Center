import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl  # Importar QUrl
from threading import Thread
from subprocess import Popen

def run_flask():
    """Função para rodar o servidor Flask"""
    Popen(["python", "app.py"])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicativo Flask")
        self.setGeometry(100, 100, 800, 600)

        # Remove as bordas e barras do navegador
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Carrega a página do servidor Flask
        self.browser = QWebEngineView()
        # Corrigir o uso de setUrl, criando um objeto QUrl
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))  # Usando QUrl aqui
        self.setCentralWidget(self.browser)
        self.setWindowFlags(Qt.Window)
if __name__ == "__main__":
    # Criar uma thread para rodar o Flask em paralelo
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
