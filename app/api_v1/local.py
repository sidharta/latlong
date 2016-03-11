from flask import jsonify, request, json, Response

from google.appengine.ext import ndb
import datetime

from google.appengine.api import channel

from . import api
from ..models.local import Local


@api.route('/locals', methods=['POST'])
def create_local( ):
    local = Local(
        key = request.json['key'],
        lat = request.json['lat'],
        lng = request.json['lng']
    )
    local.put()
    channel.send_message('latlong', request.data)
    return 'Recebido! {}'.format(local)


@api.route('/locals/latest/<key>', methods=['GET'])
def get_local( key ):
    local = Local.query(Local.key==key).order(-Local.date)
    return Response(response=json.dumps([l.to_dict() for l in local.fetch(1)]),
                    status=200,
                    mimetype="application/json");


@api.route('/locals/history/<key>', methods=['GET'])
def get_local_history( key ):
    local = Local.query(Local.key==key).order(-Local.date)
    return Response(response=json.dumps([l.to_dict() for l in local.fetch(100)]),
                    status=200,
                    mimetype="application/json");

@api.route('/locals/delete', methods=['GET'])
def delete(  ):
    ndb.delete_multi(
        Local.query().fetch(keys_only=True)
    )
    return 'OK';
