import os
import pymongo
import datetime
from os.path import join, dirname
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()
MongoDbAtlas = os.environ.get("MongoDbAtlas")

class ConnectionDatasetResults:
    def __init__(self):
        self.stringSecret = MongoDbAtlas
        self.myclient = pymongo.MongoClient(self.stringSecret)
        self.mydb = self.myclient["IBLUEIT"]
        
    def get_all_pacients(self, pacientTestId):
        mycol = self.mydb["pacients"]
        if(pacientTestId):
            pacients = mycol.find({'_id': {"$ne" : ObjectId(pacientTestId)}})
        else:
            pacients = []
        return pacients

    def get_plataform_overviews_for_pacient(self, pacientId):
        mycol = self.mydb["plataformoverviews"]
        try:
            plataformoverviews = mycol.find({"pacientId": pacientId}).sort([('timestamp', -1)]).limit(1)
            plataformoverviews = [ plataformoverview for plataformoverview in plataformoverviews ]
            if len(plataformoverviews) == 0:
                plataformoverviews = [{ "duration": 90, "result": 0, "stageId": 1, "phase": 1, "level": 1 }]
        except:
            plataformoverviews = [{ "duration": 90, "result": 0, "stageId": 1, "phase": 1, "level": 1 }]
        return plataformoverviews[0]
    
    def pacientTestInformations(self, pacientTestId):
        mycol = self.mydb["pacients"]
        if(pacientTestId):
            pacients = mycol.find({"_id": ObjectId(pacientTestId)})
            pacient = [ pacient for pacient in pacients ][0]
            year = datetime.date.today().year - pacient.get('birthday').year
            plataformoverviews = self.get_plataform_overviews_for_pacient(str(pacient.get('_id')))
            pacientResult = {
                "pacientId": pacientTestId,
                "pacientName": pacient.get('name'),
                "year": year,
                "height": pacient.get('height'),
                "weight": pacient.get('weight'),
                "sex": pacient.get('sex'),
                "condition": pacient.get('condition'),
                "insPeakFlow": pacient.get('capacitiesPitaco').get("insPeakFlow"),
                "insFlowDuration": pacient.get('capacitiesPitaco').get("insFlowDuration"),
                "expPeakFlow": pacient.get('capacitiesPitaco').get("expPeakFlow"),
                "expFlowDuration": pacient.get('capacitiesPitaco').get("expFlowDuration"),
                "respiratoryRate": pacient.get('capacitiesPitaco').get("respiratoryRate"),
                "duration_game": plataformoverviews.get('duration'),
                "result": plataformoverviews.get('result'),
                "stageId": plataformoverviews.get('stageId'),
                "phase": plataformoverviews.get('phase'),
                "level":plataformoverviews.get('level')
            }
        else:
            pacientResult = {}
        return pacientResult

    def get_datasetResults(self, pacientTestId):
        pacients = self.get_all_pacients(pacientTestId)

        datasetResults = []
        for pacient in pacients:
            datasetResult = {
                "pacientId": None,
                "pacientName": None,
                "year": None,
                "height": None,
                "weight": None,
                "sex": None,
                "condition": None,
                "insPeakFlow": None,
                "insFlowDuration": None,
                "expPeakFlow": None,
                "expFlowDuration": None,
                "respiratoryRate": None,
                "duration_game": None,
                "result": None,
                "stageId": None,
                "phase": None,
                "level": None
            }
            datasetResult["pacientId"] = str(pacient.get('_id'))
            datasetResult["pacientName"] = str(pacient.get('name'))
            year = datetime.date.today().year - pacient.get('birthday').year
            datasetResult["year"] = year
            datasetResult["height"] = pacient.get('height')
            datasetResult["weight"] = pacient.get('weight')
            datasetResult["sex"] = pacient.get('sex')
            datasetResult["condition"] = pacient.get('condition')
            datasetResult["insPeakFlow"] = pacient.get('capacitiesPitaco').get("insPeakFlow")
            datasetResult["insFlowDuration"] = pacient.get('capacitiesPitaco').get("insFlowDuration")
            datasetResult["expPeakFlow"] = pacient.get('capacitiesPitaco').get("expPeakFlow")
            datasetResult["expFlowDuration"] = pacient.get('capacitiesPitaco').get("expFlowDuration")
            datasetResult["respiratoryRate"] = pacient.get('capacitiesPitaco').get("respiratoryRate")
            plataformoverviews = self.get_plataform_overviews_for_pacient(str(pacient.get('_id')))
            datasetResult['duration_game'] = plataformoverviews.get('duration')
            datasetResult['result'] = plataformoverviews.get('result')
            datasetResult['stageId'] = plataformoverviews.get('stageId')
            datasetResult['phase'] = plataformoverviews.get('phase')
            datasetResult['level'] = plataformoverviews.get('level')
            datasetResults.append(datasetResult)

        return datasetResults