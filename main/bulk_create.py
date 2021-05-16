from .main.models import Lawyer
from django.contrib.auth.models import User


class FakeLawyer:
    def __init__(self, fname, lname, phone, email, password):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.password = password


lawyers = [
    FakeLawyer(fname="shande", lname="jimoh", phone="09011111111",
               email="shade@jimoh.com", password="123456789"),
    FakeLawyer(fname="festus", lname="chukwu", phone="09022222222",
               email="festus@chukwu.com", password="123456789"),
    FakeLawyer(fname="emeka", lname="kabiru", phone="09033333333",
               email="emeka@kabiru.com", password="123456789"),
    FakeLawyer(fname="chuks", lname="adam", phone="09044444444",
               email="chuks@adam.com", password="123456789"),
    FakeLawyer(fname="chioma", lname="okoye", phone="09055555555",
               email="chioma@okoye.com", password="123456789"),
    FakeLawyer(fname="fatima", lname="nuhu", phone="09066666666",
               email="fatima@nuhu.com", password="123456789")

]


def register_lawyer(lawyer):
    lawyer = Lawyer().create(firstname=lawyer.fname, lastname=lawyer.lname, phone=lawyer.phone,
                             password=lawyer.password, email=lawyer.email)


for lawyer in lawyers:
    register_lawyer(lawyer)