from flask import Flask, render_template, request

from Task6.pep8_checker import Pep8Checker

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/pep8_check', methods=['GET', 'POST'])
def pep8_check():
    if request.method == 'POST':
        text = request.form.get('text')
        pep8_checker = Pep8Checker(text)
        result_text = pep8_checker.get_text()
        lines_numeration = pep8_checker.get_lines_numeration()
        mistakes_string = pep8_checker.get_mistakes_string()

        if mistakes_string.isspace() or mistakes_string == "":
            mistakes_string = "Файл соответсвует стандартам pep8"

        return render_template('checker.html', text=result_text, mistakes=mistakes_string,
                               lines_numeration=lines_numeration)
    return render_template('checker.html', text="", mistakes="", lines_numeration="")


if __name__ == "__main__":
    app.run()
