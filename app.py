from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

tasks = [
    {
        'id': 1,
        'title': 'title_1',
        'description': 'description_1', 
        'done': False
    },
    {
        'id': 2,
        'title': 'title_2',
        'description': 'description_2', 
        'done': False
    }
]

@app.route('/')
def index():
    return "Hello, World!"
    
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify({ 'tasks': tasks })

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):

    task = list(filter(lambda t: t['id'] == task_id, tasks))

    if len(task) == 0:
        abort(404)

    return jsonify( { 'task': task[0]) } )

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():

    if not request.json or not 'title' in request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)

    return jsonify( { 'task': task } ), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):

    task = list(filter(lambda t: t['id'] == task_id, tasks))

    if len(task) == 0 or if not request.json:
        abort(404)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify( { 'task': task } )
    
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):

    task = list(filter(lambda t: t['id'] == task_id, tasks))

    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])

    return jsonify( { 'result': True } )
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
