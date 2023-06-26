from flask import jsonify, request
from models.models import *
from utils.utils import checktoken
import json

OK = 'ok'
NOT_AVAILABLE_AT_CLOUD  = { 'result': 'error, funcio no disponible al cloud' }
NOT_AVAILABLE_AT_EDGE   = { 'result': "error, funcio no disponible a l'edge" }

def beehives_global():

    if is_local == 1:
        return jsonify(NOT_AVAILABLE_AT_EDGE)

    data = request.get_json()
    value = checktoken(data['session_token'])
    response = { 'value' : value['valid'] }
<<<<<<< Updated upstream
=======

    if value['valid'] == OK:
        colmenitas = colmenas.find()
>>>>>>> Stashed changes

    if value['valid'] == OK:
        colmenitas = colmenas.find()
        beehives = []
        for colmena in colmenitas:
            beehives.append({
                'id_beehive'    : colmena['id_beehive'],
                'latitude'      : colmena['location_end']['latitude'],
                'longitude'     : colmena['location_end']['longitude'],
                'url beehive'   : "/api/beehives/global",
            })
        response['beehives'] = beehives
    else:
        response = value 

    return jsonify(response) 

def beehives_local():

    if is_local == 0:
        return jsonify(NOT_AVAILABLE_AT_CLOUD)

    data = request.get_json()
    value = checktoken(data['session_token'])
    response = { 'value' : value['valid'] }

    if value['valid'] == OK:
        colmenitas = colmenas.find()

        beehives = []
        for colmena in colmenitas:
            beehives.append({
                'id_beehive'    : colmena['id_beehive'],
                'latitude'      : colmena['location_end']['latitude'],
                'longitude'     : colmena['location_end']['longitude'],
            })
        response['beehives'] = beehives
    else:
        response = value
        
    return jsonify(response) 
