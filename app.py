import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Note

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add", methods=['POST'])
def add_note():
    title=request.form['title']
    content=request.form['content']
    author=request.form['author']
    published=request.form['published']
    try:
        note=Note(
            title=title,
            content=content,
            author=author,
            published=published
        )
        db.session.add(note)
        db.session.commit()
        return "Note added. note id={}".format(note.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        notes=Note.query.all()
        return  jsonify([e.serialize() for e in notes])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>", methods = ['GET', 'POST', 'DELETE'])
def note_id(id_):
    if request.method == 'GET':
        try:
            note=Note.query.filter_by(id=id_).first()
            return jsonify(note.serialize())
        except Exception as e:
            return(str(e))
    if request.method == 'POST':
        try:
            note=Note.query.filter_by(id=id_).first()
            title=request.form['title']
            content=request.form['content']
            author=request.form['author']
            published=request.form['published']
            try:
                if not(len(title) is 0):
                    note.title=title,
                if not(len(content) is 0):
                    note.content=content,
                if not(len(author) is 0):
                    note.author=author,
                if not(len(published) is 0):
                    note.published=published
                db.session.commit()
                return "Note updated. note id={}".format(note.id)
            except Exception as e:
                return(str(e))
        except Exception as e:
            return(str(e))
    if request.method == 'DELETE':
            try:
                note=Note.query.filter_by(id=id_).first()
                db.session.delete(note)
                db.session.commit()
                return "Note deleted. note id={}".format(id_)
            except Exception as e:
                return(str(e))

if __name__ == '__main__':
    app.run()