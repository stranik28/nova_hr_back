from flask import Flask, render_template, request, redirect, jsonify
from sqlalchemy import create_engine, MetaData, Table, String, Integer, Column, Text, DateTime, Boolean,update, Float
import pymysql

def connect():
    engine = create_engine("mysql+pymysql://stranik:n01082002@localhost/nova")
    engine.connect()
    return engine

metadata = MetaData()

rev = Table('rev', metadata,
    Column('id', Integer, primary_key=True),
    Column('calendar', String(50)),
    Column('fio', String(50)),
    Column('Skills', String(50)),
    Column('Type_of_work', String(50)),
    Column('Level', String(50)),
    Column('hard', Float),
    Column('soft', Float),
    Column('full_Artemsm67', Text),
    Column('full_reaL_IdpNik', Text),
    Column('full_cris_tee', Text),
    Column('full_foxyess2020', Text),
    Column('hard_foxyess2020', Integer),
    Column('hard_Artemsm67', Integer),
    Column('hard_reaL_IdpNik', Integer),
    Column('hard_cris_tee', Integer),
    Column('soft_Artemsm67', Integer),
    Column('soft_reaL_IdpNik', Integer),
    Column('soft_cris_tee', Integer),
    Column('soft_foxyess2020', Integer),
    Column('date', DateTime),
    Column('record', String(128))
)

def isNaN(num):
    return (num != num) | (num is None)

def check_is_none(value):
    if isNaN(value):
        return "-"
    else:
        return value

app = Flask(__name__)

@app.route('/')
def index():
    engine = connect()
    sel = rev.select()
    res = engine.execute(sel)
    answ = res.fetchall()
    list = []
    for i in answ:
        d = {}
        d['id'] = check_is_none(i[0])
        d['calendar'] = check_is_none(i[1])
        d['fio'] = check_is_none(i[2])
        d['Skills'] = check_is_none(i[3])
        d['Type_of_work'] = check_is_none(i[4])
        d['Level'] = check_is_none(i[5])
        d['hard'] = check_is_none(i[6])
        d['soft'] = check_is_none(i[7])
        d['full_Artemsm67'] = check_is_none(i[8])
        d['full_reaL_IdpNik'] = check_is_none(i[9])
        d['full_cris_tee'] = check_is_none(i[10])
        d['full_foxyess2020'] = check_is_none(i[11])
        d['hard_foxyess2020'] = check_is_none(i[12])
        d['hard_Artemsm67'] = check_is_none(i[13])
        d['hard_reaL_IdpNik'] = check_is_none(i[14])
        d['hard_cris_tee'] = check_is_none(i[15])
        d['soft_Artemsm67'] = check_is_none(i[16])
        d['soft_reaL_IdpNik'] = check_is_none(i[17])
        d['soft_cris_tee'] = check_is_none(i[18])
        d['soft_foxyess2020'] = check_is_none(i[19])
        d['date'] = check_is_none(i[20])
        d['record'] = check_is_none(i[21])
        list.append(d)
    print(list)
    return render_template('index.html', list=list)

app.run()