class Pep8Checker:
    _text_lines = []
    _mistakes = []

    def __init__(self, input_text: str):
        self._text_lines = input_text.split("\n")
        self._mistakes = []

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

    def check_indentation(self):
        self._text_lines = self._check_redundant_whitespaces()  # можно сразу исправить(не факт)
        self._text_lines = self.check_def_whitespaces()  # можно сразу исправить(пробелы между аргументами и тд)
        self._text_lines = self._check_def_blank_lines()  # можно сразу исправить
        self._check_maximum_line_length()
        self._check_imports()
        self._text_lines = self._check_file_ending_with_blank_line()  # можно сразу исправить

    def check_naming(self):
        line_index = 1
        for line in self._text_lines:
            if "class" in line:
                self._check_class_naming(line, line_index)

            elif "def" in line:
                self._check_def_naming(line, line_index)

            elif "=" in line:
                self._check_variable_naming(line, line_index)

            line_index += 1

    def _check_redundant_whitespaces(self):
        text_lines = self._text_lines

        result_lines = []
        for line in text_lines:

            result_line = " ".join(line.split())

            if result_line != "":
                result_lines.append(result_line)

        return result_lines

    def check_def_whitespaces(self):
        text_lines = self._text_lines

        result_lines = []
        def_is_active = False
        for line in text_lines:

            if ":" in line:
                def_is_active = True
                result_lines.append(line)
                continue

            if def_is_active:
                line = " ".join(line.split())
                line = "    " + line

            result_lines.append(line)
        return result_lines

    def _check_maximum_line_length(self):
        text_lines = self._text_lines
        return

    def _check_def_blank_lines(self):
        text_lines = self._text_lines

        result_lines = []
        for line in text_lines:

            operands = line.split(" ")
            if operands[0] == "\r":
                continue

            if operands[0] == "def" and line is not text_lines[0]:
                result_lines.append("")

            result_lines.append(line)
        return result_lines

    def _check_file_ending_with_blank_line(self):
        result_lines = self._text_lines

        last_line_index = len(result_lines) - 1
        last_line = result_lines[last_line_index]

        if not last_line.isspace():
            result_lines.append("")

        return result_lines

    def _check_def_naming(self, line, line_index):
        splitted = line.split()

        if splitted[0] == "def":
            function_name_and_args = splitted[1]
            function_name = function_name_and_args.split("(")[0].strip()

            if not function_name.islower():
                self._mistakes.append(f"Incorrect function naming in line: {line_index}")

    def _check_class_naming(self, line, line_index):
        splitted = line.split()

        if splitted[0] == "class":
            class_name = splitted[1]

            if "_" in class_name or not class_name[0].isupper():
                self._mistakes.append(f"Incorrect class naming in line: {line_index}")

    def _check_variable_naming(self, line, line_index):
        splitted = []
        if "==" in line:
            splitted = line.split("==")
        else:
            splitted = line.split("=")
        variable_name = splitted[0].strip()

        if not variable_name.islower():
            self._mistakes.append(f"Incorrect variable naming in line: {line_index}")

    def _check_imports(self):
        return
