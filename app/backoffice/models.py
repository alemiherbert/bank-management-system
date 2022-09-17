from app import db
from datetime import datetime
from math import floor
from random import random, seed
def gen_num(bid: str, nin: str) -> str:
    seed(nin)
    return bid + str(floor(random() * 10000)).rjust(5, '0')


class Branch(db.Model):
    __tablename__ = "branch"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    rcode = db.Column(db.String(4), nullable=False, index=True, unique=True)
    accounts = db.relationship("Account", backref="homebranch", foreign_keys="Account.branch_id")
    customers = db.relationship("Customer", backref="homebranch", foreign_keys="Customer.cbranch_id")
    employees = db.relationship("Employee", backref="workbranch", foreign_keys="Employee.ebranch_id")
    
    def __init__(self, bdata):
        self.name = bdata["name"]
        self.rcode = bdata["rcode"]
    def __repr__(self):
        return f"<Branch: {self.name}>"



class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(32), nullable=False, index=True)
    status = db.Column(db.Integer, nullable=False, index=True)    
    number = db.Column(db.String(32), nullable=False, index=True)    
    balance = db.Column(db.String(32))
    holder_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.id"))
    createdate = db.Column(db.DateTime, index=True, default=datetime.utcnow)    

    def __init__(self, adata):
        self.kind = adata["kind"]
        self.status = 1
        self.homebranch = adata["branch"]
        self.balance = "0000000"
        self.holder = adata["holder"]
        self.number = gen_num(adata["branch"].rcode, int(adata["nin"]))

    def __repr__(self):
        return f"<Account: {self.number}>"


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(32), nullable=False)
    lname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False, index=True, unique=True)
    phone = db.Column(db.String(32), nullable=False, index=True, unique=True)
    nin = db.Column(db.String(32), nullable=False, index=True, unique=True)
    gender = db.Column(db.String(32), nullable=False)
    d_o_b = db.Column(db.Date, default=datetime.utcnow)
    address = db.Column(db.String(128), nullable=False)
    occupation = db.Column(db.String(32), nullable=False)
    status = db.Column(db.Integer, nullable=False, index=True)
    accounts = db.relationship("Account", backref="holder")
    cbranch_id = db.Column(db.Integer, db.ForeignKey("branch.id"))
    ctype = db.Column(db.String(32), nullable=False, index=True)
    joindate = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    __mapper_args__ = {"polymorphic_identity":"customer","polymorphic_on":ctype}

    def get_data(self):
        data = {}
        hidden_attrs = ["_sa_instance_state", "ctype"]
        for key, value in self.__dict__.items():
            if key not in hidden_attrs:
                data[key] = value
        return data  

    def __init__(self, cdata):
        self.fname = cdata["fname"]
        self.lname = cdata["lname"]
        self.email = cdata["email"]
        self.phone = cdata["phone"]
        self.gender = cdata["gender"]
        self.address = cdata["address"]
        self.d_o_b = cdata["d_o_b"]
        self.nin = cdata["nin"]
        self.occupation = cdata["occupation"]
        self.status = 1
        self.homebranch = cdata["branch"]


    def __repr__(self):
        return f"<Customer: {self.fname}>"



class Employee(Customer):
    __tablename__ = "employee"
    id = db.Column(db.Integer, db.ForeignKey("customer.id", ondelete="CASCADE"), primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    e_id = db.Column(db.String(32), nullable=False, index=True, unique=True)
    estatus = db.Column(db.Integer, nullable=False, index=True)
    ebranch_id = db.Column(db.Integer, db.ForeignKey("branch.id"))
    startdate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    __mapper_args__ = {"polymorphic_identity": "employee"}
    
    def __init__(self, cdata, pdata):
        # cdata is customer data from Customer.get_data()
        # edata is position data from Position.get_data()
        super().__init__(cdata)
        self.title = pdata["title"]
        self.estatus = 1
        self.e_id = self.fname.upper() + self.lname.upper() + str(self.id).rjust(4, "0")
        self.workbranch = pdata["branch"]

    def __repr__(self):
        return f"<Employee: {self.fname}, {self.title}>"
