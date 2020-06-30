from paskey import db

class Keys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(150), nullable=False)
    key = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return f"Keys('{self.link}','{self.key}')"