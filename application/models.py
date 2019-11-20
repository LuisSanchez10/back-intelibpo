from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Calls(db.Model):
    __tablename__ = 'calls'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    call_time = db.Column(db.DateTime(timezone=True))
    duration_call = db.Column(db.Integer())
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id', ondelete='CASCADE'), nullable=False)
    topic = db.relationship('Topics')

    def __init__(self, first_name, last_name, call_time, duration_call, topic_id):
        self.first_name = first_name
        self.last_name = last_name
        self.call_time = call_time
        self.duration_call = duration_call
        self.topic_id = topic_id

class Topics(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
