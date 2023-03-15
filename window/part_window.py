from PyQt6.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout
from PyQt6.QtCore import QAbstractTableModel, Qt


class MyModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole:
            row = index.row()
            col = index.column()
            return self._data[row][col]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    # dummy data to display in the table
    data = [['row {} col {}'.format(i+1, j+1) for j in range(10)] for i in range(5)]

    # create and set the model
    model = MyModel(data)

    # create the table view and set the model
    table_view = QTableView()
    table_view.setModel(model)

    # add the table view to the layout
    layout.addWidget(table_view)

    # set the layout on the window and show
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
