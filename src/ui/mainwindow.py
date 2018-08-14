from PyQt5.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.picture import PicturesCollection


class MainWindow(QWidget):
    def __init__(self, title=''):
        super().__init__()

        self.initUI(title)

    def initUI(self, title):
        src_hbox = QHBoxLayout()
        src_hbox.addStretch(1)
        src_folder_label = QLabel('Carpeta a ordenar')
        src_hbox.addWidget(src_folder_label)
        self.input_path_text = QLineEdit()
        src_hbox.addWidget(self.input_path_text)
        self.input_path_button = QPushButton('Browse')
        src_hbox.addWidget(self.input_path_button)

        dst_hbox = QHBoxLayout()
        dst_hbox.addStretch(1)
        src_folder_label = QLabel('Nueva carpeta para fotos ordenadas')
        dst_hbox.addWidget(src_folder_label)
        self.output_path_text = QLineEdit()
        dst_hbox.addWidget(self.output_path_text)
        self.output_path_button = QPushButton('Browse')
        dst_hbox.addWidget(self.output_path_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(src_hbox)
        vbox.addLayout(dst_hbox)

        self.organise_button = QPushButton('Organise')
        vbox.addWidget(self.organise_button)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 600, 150)
        self.setWindowTitle(title)

        self.input_path_button.clicked.connect(self.on_browse_input)
        self.output_path_button.clicked.connect(self.on_browse_output)
        self.organise_button.clicked.connect(self.on_organise)

        self.show()

    def on_output_changed(self):
        pass

    def on_input_changed(self):
        pass

    def on_organise(self):
        src = self.get_source_path()
        dest = self.get_dest_path()
        picture_collection = PicturesCollection(src)
        picture_collection.sort_into_folder(dest)

    def get_source_path(self):
        return self.input_path_text.text()

    def get_dest_path(self):
        return self.output_path_text.text()

    def update_source_path(self, source_path):
        self.input_path_text.setText(source_path)

    def update_dest_path(self, source_path):
        self.output_path_text.setText(source_path)

    def on_browse_input(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.update_source_path(path)

    def on_browse_output(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.update_dest_path(path)
