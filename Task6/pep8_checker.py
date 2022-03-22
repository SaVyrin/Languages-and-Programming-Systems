import re


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
        self._text_lines = self._check_duplicate_whitespaces()  # TODO : готово
        self._text_lines = self._check_comments()  # TODO : готово
        self._text_lines = self._check_parenthesis("\(", "\)")  # проверить
        self._text_lines = self._check_parenthesis("\[", "\]")  # проверить
        self._text_lines = self._check_parenthesis("\{", "\}")  # проверить
        # check multi line arguments
        # check ; :
        # check = + - / * ** % //
        # check one line constructions (constructions after :)

        self._text_lines = self._check_imports()  # TODO : готово
        self._text_lines = self._check_redundant_blank_lines()  # проверить
        self._text_lines = self._check_def_blank_lines()  # проверить
        self.check_left_whitespaces_count()  # TODO : готово
        self._text_lines = self._check_file_ending_with_blank_line()  # TODO : готово
        self._check_maximum_line_length()  # TODO : готово

    def check_naming(self):
        line_index = 1
        for line in self._text_lines:
            if "class" in line.split():
                self._check_class_naming(line, line_index)

            elif "def" in line.split():
                self._check_def_naming(line, line_index)

            elif "=" in line.split():
                self._check_variable_naming(line, line_index)

            line_index += 1

    def _check_duplicate_whitespaces(self):
        text_lines = self._text_lines

        result_lines = []
        for line in text_lines:
            spaces = ""
            for sign in line:
                if sign != " ":
                    break
                spaces += " "

            result_line = " ".join(line.split())
            result_line = spaces + result_line

            result_lines.append(result_line)

        return result_lines

    def _check_comments(self):
        text_lines = self._text_lines

        result_lines = []
        for line in text_lines:
            result_line = line

            if "#" in line:
                comment_line = line.split("#")
                comment = comment_line[1]
                comment = comment.strip()
                result_line = f"# {comment}"

                if comment_line[0] != "" and not comment_line[0].isspace():
                    result_line = comment_line[0].rstrip() + "  " + result_line
                else:
                    result_line = comment_line[0] + result_line

            result_lines.append(result_line)

        return result_lines

    def check_left_whitespaces_count(self):
        line_index = 1
        for line in self._text_lines:
            left_spaces_count = 0
            for sign in line:
                if sign != " ":
                    break
                left_spaces_count += 1

            if left_spaces_count % 4 != 0:
                self._mistakes.append(
                    f"Indentation is not multiple for four({left_spaces_count}) in line: {line_index}")

            line_index += 1

    def _check_maximum_line_length(self):
        line_index = 1
        for line in self._text_lines:
            if len(line) > 79:
                self._mistakes.append(f"Too long line in line: {line_index}")
            line_index += 1

    def _check_redundant_blank_lines(self):
        text_lines = self._text_lines

        result_lines = []
        in_class = False
        blank_lines_count = 0
        for line in text_lines:
            if line.isspace() or line == "":
                if in_class and blank_lines_count == 1:
                    continue
                elif not in_class and blank_lines_count == 2:
                    continue
                else:
                    result_lines.append(line)
                    blank_lines_count += 1
                    continue
            else:
                blank_lines_count = 0
                result_lines.append(line)

            operands = line.split()
            if operands[0] == "class":
                in_class = True

            if operands[0] != "class" and in_class and line[0] != " ":
                in_class = False

        return result_lines

    def _check_parenthesis(self, parenthesis1, parenthesis2):
        result_lines = []

        for line in self._text_lines:
            result_line = line
            result = re.findall(f"{parenthesis1}(.*?){parenthesis2}", line)
            result_in_string = re.search(f"\".*{parenthesis1}(.*?){parenthesis2}.*\"", line)

            if result is not None and result_in_string is None:
                for res in result:
                    arguments = res
                    result_line = result_line.replace(arguments, arguments.strip())
            result_lines.append(result_line)

        return result_lines

    def _check_def_blank_lines(self):
        text_lines = self._text_lines

        result_lines = []
        in_class = False
        blank_lines_count = 0
        for line in text_lines:
            if line.isspace() or line == "":
                blank_lines_count += 1
                result_lines.append(line)
                continue

            operands = line.split()
            if operands[0] != "def":
                blank_lines_count = 0

            if operands[0] == "class":
                in_class = True

            if operands[0] != "class" and in_class and line[0] != " ":
                in_class = False

            if operands[0] == "def" and line is not text_lines[0]:
                if in_class and blank_lines_count < 1:
                    result_lines.append("")
                elif not in_class and blank_lines_count < 2:
                    needed_blank_lines_count = 2 - blank_lines_count
                    for blank_line in range(0, needed_blank_lines_count):
                        result_lines.append("")

            result_lines.append(line)
        return result_lines

    def _check_file_ending_with_blank_line(self):
        result_lines = self._text_lines

        last_line_index = len(result_lines) - 1
        if last_line_index >= 0:
            last_line = result_lines[last_line_index]

            if not last_line.isspace() and not last_line == "":
                result_lines.append("")

        return result_lines

    def _check_imports(self):
        result_lines = []

        line_index = 1
        last_import = ""
        for line in self._text_lines:

            line_array = line.split()
            if "import" in line_array:
                if "from" not in line_array:
                    line_array = line.split()
                    if len(line_array) > 2:
                        self._mistakes.append(f"Incorrect importing in line: {line_index}")
                last_import = line

            elif last_import != "":
                result_lines.append("")
                result_lines.append("")
                last_import = ""

            line_index += 1
            result_lines.append(line)

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
