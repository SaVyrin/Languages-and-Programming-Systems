from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QGroupBox, QRadioButton

settings_style_sheet = """
SettingsWindow {
    border-image: url(Resources/images/bckg.jpg) 0 0 0 0 stretch stretch;
}
QPushButton {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #111;
}

QPushButton:hover {
    background-color: rgba(183, 30, 28, 0.8);
    border: 3px solid #111;
}
QPushButton:pressed {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #aaa;
}
QRadioButton::indicator::unchecked 
{
    background-color: rgba(232, 228, 216, 0.8);
    border: 1px solid #222;
    border-radius: 8px;
}
QRadioButton::indicator::checked 
{
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid rgba(183, 30, 28, 0.8);
    border-radius: 8px;
}
"""


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window, game_settings):
        super(SettingsWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/settings.ui', self)

        self.setStyleSheet(settings_style_sheet)
        self.setWindowIcon(QtGui.QIcon('Resources/images/icon.png'))

        self._check_actual_settings_radio_buttons(game_settings)
        self.menuButton.clicked.connect(self._menu_btn_clicked)
        self.saveSettingsButton.clicked.connect(self._change_settings_btn_clicked)
        self._remove_group_boxes_border()

    def _check_actual_settings_radio_buttons(self, game_settings):
        field_colors_group: QGroupBox = self.fieldColors
        field_colors = field_colors_group.children()

        color_mode = str(game_settings["color_mode"] + 1)
        radio_button: QRadioButton
        for radio_button in field_colors:
            radio_text = radio_button.text()
            if color_mode in radio_text:
                radio_button.setChecked(True)

        field_sizes_group: QGroupBox = self.fieldSizes
        field_sizes = field_sizes_group.children()

        rows_count = game_settings["rows_count"]
        cols_count = game_settings["cols_count"]
        size = str(cols_count) + " x " + str(rows_count)
        radio_button: QRadioButton
        for radio_button in field_sizes:
            radio_text = radio_button.text()
            if size in radio_text:
                radio_button.setChecked(True)

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
