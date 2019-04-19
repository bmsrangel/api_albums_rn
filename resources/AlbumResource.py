from flask import jsonify, request
from flask_restful import Resource
from Model import db, Album, AlbumSchema

albums_schema = AlbumSchema(many=True)
album_schema = AlbumSchema()


class AlbumResource(Resource):
    def get(self):
        albums = Album.query.all()
        albums = albums_schema.dump(albums).data
        return {"status": "success", "data": albums}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = album_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        album = Album(
            title=data['title'], artist=data['artist'], url=data['url'], image=data['image'], thumbnail=data['thumbnail']
        )
        db.session.add(album)
        db.session.commit()

        result = album_schema.dump(album).data

        return {'status': "success", 'data': result}, 201
