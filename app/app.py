from flask import Flask, jsonify
from app import DataBase

# create Flask object called app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """return all tasks

    Returns:
        [Response]: [return data as json]
    """
    return jsonify(DataBase.get_todos())


@app.route('/add/<string:content>/<int:status>', methods=['POST'])
def add_todo(content: str, status: int):
    """EndPoint for add new task

    Args:
        content (str): [content of task]
        status (int): [status of task and must be integer between [0,2]]

    Raises:
        Exception: [if status out of range]

    Returns:
        [response]: [return response as json]
    """

    try:
        added = DataBase.add_todo(content, status)

        if not added:
            raise Exception("invalid status range")

        response = {
            'status': 200,
            'response': 'todo added Done'
        }

    except Exception as e:
        response = {
            'status': 400,
            'response': 'invalid to add todo',
            'Eroor': str(e)
        }

    return jsonify(response)


@app.route('/update/<string:content>/<int:status>/<int:id>', methods=['PATCH'])
def update(content: str,  status: int, id: int):
    """update task by id

    Args:
        content (str): [new content to task]
        status (int): [new status to task]
        id (int): [uuid of task we want to update]

    Raises:
        Exception: [if new status out of range [1]]
        Exception: [if id of task not found [2]]

    Returns:
        [response]: [return response as json]
    """

    try:
        updated, error = DataBase.update_todo(content, status, id)

        if not updated:
            if error == 1:
                raise Exception("invalid status range")
            else:
                raise Exception("id not found")

        response = {
            'status': 200,
            'response': 'Update Done'
        }
    except Exception as e:
        response = {
            'status': 400,
            'response': 'invalid to Update todo',
            'Eroor': str(e)
        }

    return jsonify(response)


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id: int):
    """function remove a task by id

    Args:
        id (int): [id of the task that we want to deleted]

    Raises:
        Exception: [if id of the task not found]

    Returns:
        [response]: [return response as json]
    """

    try:
        deletd = DataBase.delete_todo(id)

        if not deletd:
            raise Exception("todo has not found")

        response = {
            'status': 200,
            'response': 'Delete Done'
        }
    except Exception as e:
        response = {
            'status': 400,
            'response': 'invalid to Delete todo',
            'Eroor': str(e)
        }

    return jsonify(response)


def create_app() -> Flask:
    """ return Flask app

    Returns:
        [app]: [return Flask object]
    """
    return app
