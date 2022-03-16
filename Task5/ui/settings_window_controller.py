from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGroupBox, QRadioButton


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window):
        super(SettingsWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/settings.ui', self)

        self.menuButton.clicked.connect(self._menu_btn_clicked)
        self.saveSettingsButton.clicked.connect(self._change_settings_btn_clicked)
        self._remove_group_boxes_border()

    def _remove_group_boxes_border(self):
        field_sizes_group: QGroupBox = self.fieldSizes
        field_colors_group: QGroupBox = self.fieldColors
        field_sizes_group.setStyleSheet("border:0;")
        field_colors_group.setStyleSheet("border:0;")

    def _change_settings_btn_clicked(self):
        field_sizes_group: QGroupBox = self.fieldSizes
        field_colors_group: QGroupBox = self.fieldColors

        field_sizes = field_sizes_group.children()
        field_colors = field_colors_group.children()

        cols_count = 0
        rows_count = 0
        radio_button: QRadioButton
        for radio_button in field_sizes:
            if radio_button.isChecked():
                radio_text_array = radio_button.text().split(" ")
                cols_count = int(radio_text_array[0])
                rows_count = int(radio_text_array[2])

        color_mode = 0
        for radio_button in field_colors:
            if radio_button.isChecked():
                radio_text_array = radio_button.text().split(" ")
                color_mode = int(radio_text_array[1]) - 1

        game_settings = self.menu_window.get_game_settings()
        game_settings["color_mode"] = color_mode
        game_settings["rows_count"] = rows_count
        game_settings["cols_count"] = cols_count

    def _menu_btn_clicked(self):
        self.menu_window.show()
        self.close()
