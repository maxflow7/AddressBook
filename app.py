from flask import Flask, request, json, Response
from pymongo import MongoClient

app = Flask(__name__)

class API:
    def __init__(self, data):  
        self.client = MongoClient("mongodb://localhost:27017/")
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    

    def Insert(self, data):    
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def Show(self):                
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def Update(self):          
        filter = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def Delete(self, data):   
        filter = data['Filter']
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

    def Query(self):          
       filter = self.data['Filter']
       response = self.collection.find(filter)
       output = {'Status': 'Successfully Done' if response.count()> 0 else "Nothing was searched."}
       return output   





@app.route('/query', methods=['GET'])    
def query():
    
    data = json.loads(request.json)
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    read_obj = API(data)
    response = read_obj.Query()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/show', methods=['GET'])    
def show():
    data = json.loads(request.json)
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    read_obj = API(data)
    response = read_obj.Show()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/insert', methods=['POST'])   
def insert():

    data = json.loads(request.json)

    if data is None or data == {}  or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    create_obj = API(data)
    response = create_obj.Insert(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/update', methods=['PUT'])  
def update():
    data = json.loads(request.json)
    
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    update_obj = API(data)
    response = update_obj.Update()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/delete', methods=['DELETE'])  
def delete():
    data = json.loads(request.json)

    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    delete_obj = API(data)
    response = delete_obj.Delete(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


















