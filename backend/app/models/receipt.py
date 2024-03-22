from app.extensions import db

class Receipt(db.Model):
	__tablename__ = "receipt"
	id = db.Column(
		db.Integer, 
		primary_key=True, 
		autoincrement="auto"
	)
	claim_id = db.Column(db.Integer, db.ForeignKey("claim.id")), 
	title = db.Column(db.String(144))
	image_uri = db.Column(db.Text)

	def __repr__(self):
		return f"Receipt ID: {self.id}"
	#
#

# End of File