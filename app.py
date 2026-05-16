from flask import Flask, jsonify, request, render_template
import parser


app = Flask(__name__, template_folder='template')


@app.get('/')
def hello_world():
  return 'Hello, World!'


@app.get('/names')
def names():
    """вернет json с именами всех студентов курса """
    return jsonify({'names': parser.get_names()})


@app.get('/<hw_name>/mean_score')
def mean_score_of_hw(hw_name: str):
    """Вернет средний балл всех участников курса за домашку <hw-name>"""
    return jsonify({'mean_score': parser.get_mean_score_of_hw(hw_name)})


@app.get('/<hw_name>/<int:group_id>/mean_score')
def mean_score_of_hw_in_group(hw_name: str, group_id: int):
    """Вернет средний балл за домашку <hw-name> в группе <group_id>"""
    return jsonify({'mean_score': parser.get_mean_score_of_hw_in_group(hw_name, group_id )})


@app.get('/mean_score')
def mean_score_of_hw_in_group_qwery():
    """Вернет средний балл студентов из группы group_id курса за домашку hw_name"""
    group_id = request.args.get('group_id', type=int)
    hw_name = request.args.get('hw_name')

    return jsonify({'mean_score': parser.get_mean_score_of_hw_in_group(hw_name, group_id)})


@app.get('/mark')
def student_mark():
    """Возвращает оценку за зачетную неделю студента или среднюю по группе"""
    mark = 0

    student_name = request.args.get('student_name')
    if student_name is not None:
        mark = parser.get_student_mark(student_name)

    group_id = request.args.get('group_id', type=int)
    if group_id is not None:
        mark = parser.get_mean_group_mark(group_id)
    
    if mark != 0:
        return jsonify({'mark': mark})

    return {'status': 'error', 'message': 'вы ввели некорректные параметры'}, 400


@app.get('/course_table')
def course_table():
    hw_name = request.args.get('hw_name')
    if hw_name is None:
        return {'status': 'error', 'message': 'вы не указали имя дз'}, 400

    group_id = request.args.get('group_id', type=int)

    if group_id is not None:
        students = parser.get_group_names(group_id)
    else:
        group_id = "24137 24144"
        students = parser.get_names()

    print(students)
    return render_template('table.html', group_id=group_id, hw_name=hw_name, students=students)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008, debug=True)
    