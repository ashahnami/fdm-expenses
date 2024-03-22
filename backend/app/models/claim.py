from app.extensions import db


class Claim(db.Model):
    __tablename__ = 'claim'
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receipt_ids = db.relationship("Receipt", backref="Claim", lazy=True)

    def __repr__(self):
        return f"Claim ID: {self.id}"
    #
#
