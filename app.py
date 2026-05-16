from flask import Flask, jsonify, request
import parser

import typing

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/names')
def names():
    """вернет json с именами всех студентов курса """
    return jsonify({'names': parser.get_names()})


@app.route('/<hw_name>/mean_score')
def mean_score_of_hw(hw_name: str):
    """Вернет средний балл всех участников курса за домашку <hw-name>"""
    return jsonify({'mean_score': parser.get_mean_score_of_hw(hw_name)})


@app.route('/<hw_name>/<group_id>/mean_score')
def mean_score_of_hw_in_group(hw_name: str, group_id: str):
    """Вернет средний балл за домашку <hw-name> в группе <group_id>"""
    return jsonify({'mean_score': parser.get_mean_score_of_hw_in_group(hw_name, group_id)})


@app.route('/mean_score')
def mean_score_of_hw_in_group_qwery():
    """Вернет средний балл студентов из группы group_id курса за домашку hw_name"""
    
    group_id = request.args.get('group_id') 
    hw_name = request.args.get('hw_name')

    return jsonify({'mean_score': parser.get_mean_score_of_hw_in_group(hw_name, group_id)})


@app.route('/mark')
def student_mark():
    """Возвращает оценку за зачетную неделю студента с id <student-id>"""
    
    student_id = int(request.args.get('student_id'))
    return jsonify(parser.get_student_mark(student_id))
     

@app.route('/mark')
def mean_group_mark():
    """Вернет среднюю оценку для группы group_id"""
    group_id = request.args.get('group_id')
    pass




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
    