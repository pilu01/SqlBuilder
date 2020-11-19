# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 14:52
# @Author  : xhb
# @FileName: sqlal.py
# @Software: PyCharm


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import time

t1 = time.time()
engine = create_engine("oracle://pps:vastio@172.16.60.225:1521/orcl")

Base = automap_base()
Base.prepare(engine, reflect=True)
apply_info = Base.classes.aj_xyrxx
Session = sessionmaker(bind=engine)
session = Session()
row = session.query(apply_info).filter(apply_info.ajbh == '32050000000011020119')
print(row.one())

t2 = time.time()

print(t2-t1)


