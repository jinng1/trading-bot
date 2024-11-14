from . import data_pipeline
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

class DataRetrievalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window settings
        self.setWindowTitle('Data Retrieval Configuration')
        self.setGeometry(100, 100, 400, 250)

        # Layout
        layout = QVBoxLayout()

        # Symbol input
        self.symbol_label = QLabel('Symbol:')
        self.symbol_input = QLineEdit(self)
        self.symbol_input.setText('BTCUSDT')  # Default value

        # Interval input
        self.interval_label = QLabel('Interval:')
        self.interval_input = QLineEdit(self)
        self.interval_input.setText('1h')  # Default value

        # Start time input
        self.start_time_label = QLabel('Start Time:')
        self.start_time_input = QLineEdit(self)
        self.start_time_input.setText('1 Jan, 2022')  # Default value

        # Filename input
        self.filename_label = QLabel('Filename:')
        self.filename_input = QLineEdit(self)
        self.filename_input.setText('BTCUSDT_historical_data_1h.csv')  # Default value

        # Button to trigger the data retrieval function
        self.submit_button = QPushButton('Retrieve Data', self)
        self.submit_button.clicked.connect(self.retrieve_data)

        # Add widgets to the layout
        layout.addWidget(self.symbol_label)
        layout.addWidget(self.symbol_input)
        layout.addWidget(self.interval_label)
        layout.addWidget(self.interval_input)
        layout.addWidget(self.start_time_label)
        layout.addWidget(self.start_time_input)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.filename_input)
        layout.addWidget(self.submit_button)

        # Set layout
        self.setLayout(layout)

    def retrieve_data(self):
        # Get values from input fields
        symbol = self.symbol_input.text()
        interval = self.interval_input.text()
        start_time = self.start_time_input.text()
        filename = self.filename_input.text()

        try:
            # Trigger the download function (replace with actual call if available)
            filename = 'data_pipeline/data/' + filename
            df = data_pipeline.download_historical_data(symbol, interval, start_time, filename)
            QMessageBox.information(self, 'Success', f'Data retrieved for {symbol} with interval {interval}.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to retrieve data: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataRetrievalApp()
    window.show()
    sys.exit(app.exec_())


