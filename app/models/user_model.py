from app.extensions import db
from app.utils import utc_now
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__="users"

    id = db.Cloumn(db.Integer, primary_key=True, autonicrement=True)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String(50), nullable=False)
    role=db.Column(db.String(50), nullable=False, default="student")
    is_active=db.Column(db.boolean, default=True)
    created_at=db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }