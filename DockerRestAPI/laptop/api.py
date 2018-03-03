# Laptop Service
import flask
from flask import Flask,request
from flask_restful import Resource, Api
from pymongo import MongoClient
import pymongo

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient("db", 27017)
db = client.tododb
#list all open and close times
class listAll(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 20


        _items = db.tododb.find()
        #sort in multiple results,default it as ascending
        sort_items = _items.sort('open_time')
        #make it to limit k top
        k_items = sort_items.limit(int(top))

        items = [item for item in k_items]

        return{
        'open_time':[item['open_time'] for item in items],
        'close_time':[item['close_time'] for item in items],
        'km':[item['km'] for item in items]

        }
#List open times only
class listOpenOnly(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 20
        _items = db.tododb.find()
        sort_items = _items.sort("open_time")
        k_items = sort_items.limit(int(top))

        return{
        'open_time':[item['open_time'] for item in k_items],
        'km':[item['km'] for item in k_items]

        }
#
#
#list close times only
class listCloseOnly(Resource):
    def get(self):
         top = request.args.get("top")
         if top == None:
              top =20
         _items = db.tododb.find()
         sort_items = _items.sort("close_time")
         k_items = sort_items.limit(int(top))

         return {
         'close_time':[item['close_time'] for item in k_items],
         'km':[item['km'] for item in k_items]
         }
#
# ##################################################

#class listAllJson):
class listAlljson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
          top = 20
        _items = db.tododb.find()
        sort_items = _items.sort("open_time")
         #make it to limit k top
        k_items = sort_items.limit(int(top))

        items = [item for item in k_items]

#
        return {
        'open_time':[item['open_time'] for item in items],
        'close_time':[item['close_time'] for item in items],
        'km':[item['close_time'] for item in items] }

#listOpenOnlyJson
class listOpenOnlyjson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 20


        _items = db.tododb.find()
        sort_items = _items.sort("open_time")
        k_items = sort_items.limit(int(top))

        return {
        'open_time': [item['open_time'] for item in k_items]
        }

#listCloseOnlyJson
class listCloseOnlyjson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top =20
        #      _items = db.tododb.find()
        #      return { 'close_time': [item["close_time"] for item in _items]}
        # else:
        _items = db.tododb.find()
        sort_items = _items.sort("close_time")
        k_items = sort_items.limit(int(top))
        #actually km wont show up
        return {
        'close_time': [item["close_time"] for item in k_items]
        }
class listAllcsv(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 20 # total have 20 row
        _items = db.tododb.find()
        sort_items = _items.sort("open_time")
        k_items = sort_items.limit(int(top))

        csv = "List All Time In CSV: "
        for item in k_items:
            csv += item['km']+ ' , ' +item['open_time']+ ' , '+ item['close_time'] + ', '
        # app.logger.debug('csv:{}'.format(csv))
        return csv

class listOpenOnlycsv(Resource):
    def get(self):
        top = request.args.get('top')
        if top == None:
            top = 20

        _items = db.tododb.find()
        sort_items = _items.sort("open_time")
        k_items = sort_items.limit(int(top))

        csv = 'List Open Only in CSV: '
        #\n doesnt work here
        for item in k_items:
            csv += item['km']+' , '+item['open_time']+', '

        return csv


class listCloseOnlycsv(Resource):
    def get(self):
        top = request.args.get('top')
        if top == None:
            top = 20

        _items = db.tododb.find()
        sort_items = _items.sort("close_time")
        k_items = sort_items.limit(int(top))

        csv = 'List Close Only in CSV: '

        for item in k_items:
            csv += item['km'] + ' , ' + item['close_time']+ ', '

        # app.logger.debug('csv:{}'.format(csv))
        return csv

# Create routes
# Another way, without decorators

#first part:
api.add_resource(listAll,'/listAll')
api.add_resource(listOpenOnly,'/listOpenOnly')
api.add_resource(listCloseOnly,'/listCloseOnly')
#
# #################################################
api.add_resource(listAllcsv,'/listAll/csv')
api.add_resource(listOpenOnlycsv,'/listOpenOnly/csv')
api.add_resource(listCloseOnlycsv,'/listCloseOnly/csv')
# ########################################################
#
api.add_resource(listAlljson,'/listAll/json')
api.add_resource(listOpenOnlyjson, '/listOpenOnly/json')
api.add_resource(listCloseOnlyjson, '/listCloseOnly/json')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
