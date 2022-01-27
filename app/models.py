from . import db


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
