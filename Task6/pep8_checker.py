from Task6.pep8_corrector import Pep8Corrector
from Task6.pep8_mistakes_checker import Pep8MistakesChecker


class Pep8Checker:
    _text_lines = []
    _mistakes = []

    def __init__(self, input_text: str):
        self._text_lines = input_text.split("\n")
        self._mistakes = []
        self._text_lines = self._correct()
        self._mistakes = self._check()

    def get_text(self):
        result_text = ""
        for line in self._text_lines:
            result_text += f"{line}\n"

        return result_text

    def get_mistakes_string(self):
        result_text = ""
        for line in self._mistakes:
            result_text += line + "\n"

        return result_text

    def get_lines_numeration(self):
        lines_numeration = ""

        spaces_count = 0
        max_line_number = len(self._text_lines)
        while max_line_number > 0:
            spaces_count += 1
            max_line_number //= 10

        lines_count = len(self._text_lines)
        decrease_spaces_count_index = 10
        for line_index in range(0, lines_count):
            if (line_index + 1) == decrease_spaces_count_index:
                spaces_count -= 1
                decrease_spaces_count_index *= 10

            spaces = ""
            for space_index in range(0, spaces_count):
                spaces += " "

            lines_numeration += f"{spaces}{line_index + 1}\n"

        return lines_numeration

    def _correct(self):
        result_lines = self._text_lines
        pep8_corrector: Pep8Corrector = Pep8Corrector(result_lines)
        pep8_corrector.check_indentation()
        result_lines = pep8_corrector.get_text_lines()

        return result_lines

    def _check(self):
        pep8_mistakes_checker: Pep8MistakesChecker = Pep8MistakesChecker(self._text_lines)
        pep8_mistakes_checker.check_mistakes()
        result_mistakes = pep8_mistakes_checker.get_mistakes()

        return result_mistakes

