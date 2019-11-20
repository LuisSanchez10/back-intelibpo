from flask import jsonify
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from application.models import Calls

db = SQLAlchemy()

calls_char_topic = reqparse.RequestParser()
calls_char_topic.add_argument('start_date', required=True)
calls_char_topic.add_argument('end_date', required=True)

calls_bar_hour = reqparse.RequestParser()
calls_bar_hour.add_argument('start_date', required=True)
calls_bar_hour.add_argument('end_date', required=True)

calls_add = reqparse.RequestParser()
calls_add.add_argument('first_name', required=True)
calls_add.add_argument('last_name', required=True)
calls_add.add_argument('call_time', required=True)
calls_add.add_argument('duration_call', type=int,required=True)
calls_add.add_argument('topic_id', type=int, required=True)


class Calls_R(Resource):
    def post(self):
        args = calls_add.parse_args()
        user = Calls(first_name=args['first_name'],
                    last_name=args['last_name'],
                    call_time=args['call_time'],
                    duration_call=args['duration_call'],
                    topic_id=args['topic_id'])
        db.session.add(user)
        db.session.commit()
        return 200

class CallsTopics(Resource):
    def get(self):
        args = calls_char_topic.parse_args()
        data = db.session.execute("select c.topic_id, t.name, count(*) from calls as c \
                                    inner join topics as t on c.topic_id = t.id \
                                    where c.call_time between '%s' and '%s' \
                                    group by c.topic_id, t.name \
                                    order by c.topic_id" % (args['start_date'],args['end_date']))

        return jsonify({'data': [dict(row) for row in data]})

class CallsHours(Resource):
    def get(self):
        args = calls_char_topic.parse_args()
        data = db.session.execute("select date_part('hour', c.call_time) as hour, count(*) \
                                    from calls as c \
                                    where c.call_time between '%s' and '%s' \
                                    group by date_part('hour', c.call_time) \
                                    order by date_part('hour', c.call_time)" % (args['start_date'],args['end_date']))
        
        info = [dict(row) for row in data]
        for row in info:
            row['hour'] = int(row['hour'])

        return jsonify({'data': info})

