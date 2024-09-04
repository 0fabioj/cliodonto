import peewee as pw
from database import Database
#db = pw.MySQLDatabase("clinica", host="localhost", port=3306, user="root", passwd="1234")

class DatabaseModel(pw.Model):
    class Meta:
        database = Database().db


class Student(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    email = pw.CharField(max_length=50)
    phone = pw.CharField(max_length=20)
    status = pw.FixedCharField(max_length=1)


class Teacher(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    email = pw.CharField(max_length=50)
    phone = pw.CharField(max_length=20)
    cro = pw.CharField(max_length=20)
    status = pw.FixedCharField(max_length=1)


class Patient(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    gender = pw.FixedCharField(max_length=1)
    rg = pw.CharField(max_length=13)
    cpf = pw.CharField(max_length=11)
    birthdate = pw.DateField()
    maritalstatus = pw.FixedCharField(max_length=1)
    occupation = pw.CharField(max_length=50)
    email = pw.CharField(max_length=50)
    phone = pw.CharField(max_length=20)
    phone2 = pw.CharField(max_length=20)
    address = pw.IntegerField()
    addressnumber = pw.IntegerField()
    addresscomplement = pw.CharField(max_length=50)


class Appointment(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    patient = pw.ForeignKeyField(Patient)
    typeappt = pw.IntegerField(default=0)
    apptdate = pw.DateField()
    appttime = pw.TimeField()
    apptlen = pw.TimeField()
    student = pw.ForeignKeyField(Student)
    assistant = pw.ForeignKeyField(Student)
    teacher = pw.ForeignKeyField(Teacher)
    note1 = pw.CharField(max_length=255)
    note2 = pw.CharField(max_length=255)
    status = pw.FixedCharField(default=0, max_length=1)
    # 0-agendado, 1-iniciado, 2-finalizado, 3-cancelado
    created = pw.DateField()
    modified = pw.DateField()
    canceled = pw.DateField()


class TxType(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    status = pw.FixedCharField(max_length=1)


class Course(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    abbr = pw.CharField(max_length=15)
    status = pw.FixedCharField(max_length=1)


class Treatment(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    appt = pw.ForeignKeyField(Appointment)
    note1 = pw.CharField(max_length=255)
    txtype = pw.ForeignKeyField(TxType)
    course = pw.ForeignKeyField(Course)


class Country(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=50)
    abbr = pw.CharField(max_length=3)


class City(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=50)
    state = pw.CharField(max_length=50)
    abbr = pw.CharField(max_length=3)
    country = pw.ForeignKeyField(Country)


class ZipCode(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    address = pw.CharField(max_length=200)
    city = pw.ForeignKeyField(City)


class Graduating(DatabaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=100)
    semester = pw.IntegerField()
    year = pw.IntegerField()
    

class Enrolled(DatabaseModel):
    student = pw.ForeignKeyField(Student)
    graduating = pw.ForeignKeyField(Graduating)
    status = pw.FixedCharField(max_length=1)
    class Meta:
        primary_key = False
