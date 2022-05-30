from flask import request, Flask, jsonify
from MainGetMongoDatabase import MainGetMongoDatabase

app = Flask(__name__)


@app.route('/neighborsByPacient', methods=['GET'])
def neighborsByPacient():
    if(request.args and request.args.get('pacientId')):
        pacientTestId = request.args.get('pacientId')
    else:
        pacientTestId = ""
    mainGetMongoDatabase = MainGetMongoDatabase()
    hash_results = mainGetMongoDatabase.get_neighbors_ids(pacientTestId)

    return (jsonify(hash_results))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
