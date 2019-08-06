from flask import Flask
from flask_restplus import Api,Resource
from pymongo import MongoClient
from flask_pymongo import pymongo
from collections import defaultdict
from flask_cors import CORS

rear = MongoClient()
near = rear.movies
front=near.cinema

app = Flask(__name__)
CORS(app)
api = Api(app)



@api.route('/total')
class Theatre(Resource):
    def get(self):
        res=front.find()
        lis=[]
        for i in res:
            assign={'99popularity':i['99popularity'],'director':i['director'],'genre':i['genre'],'imdb_score':i['imdb_score'],'name':i['name']}
            lis.append(assign)
        return lis

@api.route('/a')
class Name(Resource):
    def get(self):
        res=front.find()
        list2=defaultdict(list)
        for i in res:
           list2[i['director']].append(i['name'])
        a1,a2=max(list2.items(),key=lambda x:len(x[1]))
        return {'bd':a1,'cnt':a2}


@api.route('/b')
class Fmov(Resource):
    def get(self):
        res=front.find()
        list3=defaultdict(list)
        for i in res:
            list3[i['name']].append(i['99popularity'])
        a3,a4=max(list3.items(),key=lambda x:x[1])
        return {'fmov':a3,'pop':a4}

@api.route('/c')
class Top10(Resource):
    def get(self):
        res=front.find()
        list4=defaultdict(list)
        for i in res:
            list4[i['name']].append(i['imdb_score'])
        s=sorted(list4.items(),key=lambda x:x[1],reverse=True)
        return {'top10':s[0:10]}

@api.route('/d')
class Leastm(Resource):
    def get(self):
        res=front.find()
        list5=defaultdict(list)
        for i in res:
            list5[i['name']].append(i['imdb_score'])
        s=sorted(list5.items(),key=lambda x:x[1])
        return {'least':s[0:1]}
        
@api.route('/e')
class bdir100(Resource):
    def get(self):
        res=front.find()
        list2=defaultdict(list)
        for i in res[0:101]:
           list2[i['director']].append(i['name'])
        a1,a2=max(list2.items(),key=lambda x:len(x[1]))
        return {'bestd':a1,'mname':a2}

@api.route('/f')
class bbdir100(Resource):
    def get(self):
        res=front.find()
        list2=defaultdict(list)
        for i in res[0:101]:
           list2[i['director']].append(i['imdb_score'])
        a1,a2=max(list2.items(),key=lambda x:len(x[1]))
        return {'dir':a1,'imdb_score':a2}








if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)