from app import db


class Story(db.Model):
    __tablename__ = 'storys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    text = db.Column(db.TEXT(16777215))

    annotations = db.relationship('Annotation', backref='story')

    def __repr__(self):
        return '<Book %r>' % self.name

class Annotation(db.Model):
    __tablename__ = 'annotations'

    id = db.Column(db.Integer, primary_key=True)

    story_id = db.Column(db.Integer, db.ForeignKey('storys.id'))
    comment = db.Column(db.String(4096))

    start_index = db.Column(db.Integer)
    end_index = db.Column(db.Integer)

    def __repr__(self):
        return '<Annotation %r>' % self.comment[:40]
