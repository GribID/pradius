from app import db


class Users(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_name = db.Column(db.String(20), unique=True)
    usr_pass = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    @property
    def __repr__(self):
        return '<User id: {}, Name: {}'.format(self.usr_id, self.usr_name)
