from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    patterns = db.relationship("Pattern", backref="author", lazy="dynamic")

    def __repr__(self):
        return "<User {}>".format(self.username)


class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Pattern {}>".format(self.body)


"""
tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column(
        "pattern_id", db.Integer, db.ForeignKey("pattern.id"), primary_key=True
    ),
)


class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    tags = db.relationship(
        "Tag",
        secondary=tags,
        lazy="subquery",
        backref=db.backref("pattern", lazy=True),
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
"""
