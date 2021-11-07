from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from app import db
from datetime import datetime
from app.model import name
from sqlalchemy import orm
import sqlalchemy as sql


class Scan_Name(db.Model):
    __bind_key__ = name.scan_step
    __tablename__ = "scan_name"

    id = sql.Column(sql.Integer, primary_key=True)
    
    name = sql.Column(sql.Integer(), index=True, unique=True)
    description = sql.Column(sql.Text(), index=True)

    created_at = sql.Column(sql.DateTime,index=True, default=datetime.utcnow)
    updated_at = sql.Column(sql.DateTime,index=True, default=datetime.utcnow,onupdate=datetime.utcnow)

    scan_step = orm.relationship("Scan_Step")
    scan_sub_step = orm.relationship("Scan_Sub_Step")

class Scan_Step(db.Model):
    
    __bind_key__ = name.scan_step

    __tablename__  = "scan_step"
    
    id = sql.Column(sql.Integer, primary_key=True)
    
    scan_name_id = sql.Column(sql.Integer, ForeignKey("scan_name.id"))

    order = sql.Column(sql.Integer(), index=True, unique=True)
    command = sql.Column(sql.Text(), index=True)
    short_name = sql.Column(sql.String(length=25),index=True)
    description = sql.Column(sql.Text(), index=True,)
    sub_command = sql.Column(sql.Boolean(),index=True)

    created_at = sql.Column(sql.DateTime,index=True, default=datetime.utcnow)
    updated_at = sql.Column(sql.DateTime,index=True, default=datetime.utcnow,onupdate=datetime.utcnow)
    scan_sub_step = orm.relationship("Scan_Sub_Step")

    def __repr__(self):
        return '<Scan_Step {}>'.format(str(self.order)+" - " +self.command )

class Scan_Sub_Step(db.Model):
    __bind_key__ = name.scan_step

    __tablename__ = "scan_sub_step"

    id = sql.Column(sql.Integer, primary_key=True)
    scan_name_id = sql.Column(sql.Integer, ForeignKey("scan_name.id"))
    scan_sub_step_id = sql.Column(sql.Integer, ForeignKey("scan_step.id"))


     