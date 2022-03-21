from flask import Flask, render_template, request

from Task6.pep8_checker import Pep8Checker

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        pep8_checker = Pep8Checker(text)
        pep8_checker.check_indentation()  # TODO : finish
        pep8_checker.check_naming()  # finished
        result_text = pep8_checker.get_text()
        lines_numeration = pep8_checker.get_lines_numeration()
        mistakes_string = pep8_checker.get_mistakes_string()

        return render_template('index.html', text=result_text, mistakes=mistakes_string,
                               lines_numeration=lines_numeration)
    return render_template('index.html', text="", mistakes="", lines_numeration="")


if __name__ == "__main__":
    app.run()
