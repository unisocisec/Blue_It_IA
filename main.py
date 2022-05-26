from flask import request, Flask, jsonify
from MainGetMongoDatabase import MainGetMongoDatabase

app = Flask(__name__)


@app.route('/neighborsByPacient', methods=['POST'])
def neighborsByPacient():
    request_data = request.get_json()
    pacientTestId = request_data["pacientId"]
    mainGetMongoDatabase = MainGetMongoDatabase()
    neighborsPacientIds = mainGetMongoDatabase.get_neighbors_ids(pacientTestId)

    return (jsonify({"neighborsPacientIds":neighborsPacientIds}))

if __name__ == '__main__':
    app.run()
