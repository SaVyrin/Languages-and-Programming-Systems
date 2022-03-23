import re


class Pep8MistakesChecker:
    _text_lines = []
    _mistakes = []

    def __init__(self, text_lines):
        self._text_lines = text_lines
        self._mistakes = []

    def get_mistakes(self):
        return self._mistakes

    def check_mistakes(self):
        self._mistakes = self.check_naming()
        self._mistakes = self._check_one_line_constructions()
        self._mistakes = self._check_left_whitespaces_count()
        self._mistakes = self._check_maximum_line_length()

    def check_naming(self):
        result_mistakes = self._mistakes
        line_index = 1
        for line in self._text_lines:
            if "class" in line.split():
                result_mistakes = self._check_class_naming(result_mistakes, line, line_index)

            elif "def" in line.split():
                result_mistakes = self._check_def_naming(result_mistakes, line, line_index)

            elif "=" in line.split():
                result_mistakes = self._check_variable_naming(result_mistakes, line, line_index)

            line_index += 1

        return result_mistakes

    def _check_one_line_constructions(self):
        result_mistakes = self._mistakes

        line_index = 1
        for line in self._text_lines:
            line_split = line.split()
            if re.search(f"(\".*)[;:](.*\")", line) is not None:
                continue
            if "if" in line_split or "for" in line_split or "while" in line_split:
                colon_split = line.split(":")
                right_colon_split = ""
                if len(colon_split) > 1:
                    right_colon_split = colon_split[1]
                if not right_colon_split.isspace() and right_colon_split != "":
                    result_mistakes.append(f"Multiple statements on one line(colon): {line_index}")
            if ";" in line:
                result_mistakes.append(f"Multiple statements on one line(semicolon): {line_index}")
            line_index += 1

        return result_mistakes

    def _check_left_whitespaces_count(self):
        result_mistakes = self._mistakes

        line_index = 1
        for line in self._text_lines:
            left_spaces_count = 0
            for sign in line:
                if sign != " ":
                    break
                left_spaces_count += 1

            if left_spaces_count % 4 != 0:
                result_mistakes.append(
                    f"Indentation is not multiple for four({left_spaces_count}) in line: {line_index}")

            line_index += 1

        return result_mistakes

    def _check_maximum_line_length(self):
        result_mistakes = self._mistakes

        line_index = 1
        for line in self._text_lines:
            if len(line) > 79:
                result_mistakes.append(f"Too long line in line: {line_index}")
            line_index += 1

        return result_mistakes

    def _check_imports(self):
        result_mistakes = self._mistakes

        line_index = 1
        for line in self._text_lines:

            line_array = line.split()
            if "import" in line_array:
                if "from" not in line_array:
                    line_array = line.split()
                    if len(line_array) > 2:
                        result_mistakes.append(f"Incorrect importing in line: {line_index}")

            line_index += 1

        return result_mistakes

    @staticmethod
    def _check_def_naming(mistakes, line, line_index):
        result_mistakes = mistakes

        splitted = line.split()
        if splitted[0] == "def":
            function_name_and_args = splitted[1]
            function_name = function_name_and_args.split("(")[0].strip()
            if not function_name.islower():
                result_mistakes.append(f"Incorrect function naming in line: {line_index}")

        return result_mistakes

    @staticmethod
    def _check_class_naming(mistakes, line, line_index):
        result_mistakes = mistakes

        splitted = line.split()
        if splitted[0] == "class":
            class_name = splitted[1]
            if "_" in class_name or not class_name[0].isupper():
                result_mistakes.append(f"Incorrect class naming in line: {line_index}")

        return result_mistakes

    @staticmethod
    def _check_variable_naming(mistakes, line, line_index):
        result_mistakes = mistakes

        splitted = []
        if "==" in line:
            splitted = line.split("==")
        else:
            splitted = line.split("=")
        variable_name = splitted[0].strip()

        if not variable_name.islower():
            result_mistakes.append(f"Incorrect variable naming in line: {line_index}")

        return result_mistakes
