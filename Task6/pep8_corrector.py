import re


class Pep8Corrector:
    _text_lines = []

    def __init__(self, text_lines):
        self._text_lines = text_lines

    def get_text_lines(self):
        return self._text_lines

    def check_indentation(self):
        self._text_lines = self._check_imports()

        self._text_lines = self._check_parenthesis("\(", "\)")
        self._text_lines = self._check_parenthesis("\[", "\]")
        self._text_lines = self._check_parenthesis("\{", "\}")

        self._text_lines = self._check_colon_and_semicolon()

        self._text_lines = self._check_single_math_operators()
        self._text_lines = self._check_double_math_operators()

        self._text_lines = self._check_comments()

        self._text_lines = self._check_redundant_blank_lines()
        self._text_lines = self._check_file_has_blank_lines_before_code()
        self._text_lines = self._check_def_blank_lines()
        self._text_lines = self._check_file_ending_with_blank_line()

        self._text_lines = self._check_duplicate_whitespaces()

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

    def _check_colon_and_semicolon(self):
        result_lines = []

        for line in self._text_lines:
            result_line = line
            result = re.findall(f"\s*[:;]\s*", line)

            for res in result:
                if re.search(f"(\".*){res}(.*\")", line) is not None:
                    continue
                arguments = res
                result_line = result_line.replace(arguments, arguments.strip() + " ")

            result_lines.append(result_line)

        return result_lines

    def _check_single_math_operators(self):
        result_lines = []

        for line in self._text_lines:
            result_line = line
            result = re.findall(f"\s*[+\-*/=%<>]\s*", line)

            for res in result:
                if re.search(f"(\".*){res}(.*\")", line) is not None:
                    continue
                arguments = res
                result_line = result_line.replace(arguments, " " + arguments.strip() + " ")

            result_lines.append(result_line)

        return result_lines

    def _check_double_math_operators(self):
        result_lines = []

        for line in self._text_lines:
            result_line = line

            for regex in ["(/\s+/)", "(\*\s+\*)", "(\=\s+\=)",
                          "(<\s+<)", "(>\s+>)", "(<\s+=)", "(>\s+=)",
                          "(\+\s+=)", "(\*\s+=)", "(/\s+=)", "(-\s+=)"]:
                result = re.findall(regex, line)

                for res in result:
                    if re.search(f"(\".*){res}(.*\")", line) is not None:
                        continue
                    arguments = res
                    result_line = result_line.replace(arguments, arguments.replace(" ", ""))

            result_lines.append(result_line)

        return result_lines

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

    def _check_file_has_blank_lines_before_code(self):
        index_of_first_code_line = 0
        result_lines = self._text_lines
        for line in result_lines:
            if line.isspace() or line == "":
                index_of_first_code_line += 1
            else:
                break
        result_lines = result_lines[index_of_first_code_line:]
        return result_lines

    def _check_parenthesis(self, parenthesis1, parenthesis2):
        result_lines = []

        for line in self._text_lines:
            result_line = line
            result = re.findall(f"{parenthesis1}(.*?){parenthesis2}", line)
            result_in_string = re.search(f"\".*{parenthesis1}(.*?){parenthesis2}.*\"", line)

            if result_in_string is None:
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

        for line in self._text_lines:
            line_array = line.split()
            if "import" in line_array:
                result_lines.append(line)

        result_lines.append("")
        result_lines.append("")

        for line in self._text_lines:
            line_array = line.split()
            if "import" not in line_array:
                result_lines.append(line)

        return result_lines
