from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    artist = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    thumbnail = db.Column(db.String(250), nullable=False)

    def __init__(self, title, artist, url, image, thumbnail):
        self.title = title
        self.artist = artist
        self.url = url
        self.image = image
        self.thumbnail = thumbnail


class AlbumSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    # album_id = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(1))
    artist = fields.String(required=True, validate=validate.Length(1))
    url = fields.String(required=True, validate=validate.Length(1))
    image = fields.String(required=True, validate=validate.Length(1))
    thumbnail = fields.String(required=True, validate=validate.Length(1))
