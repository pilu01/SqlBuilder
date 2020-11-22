# @Time    : 2020/11/21 上午8:13

__author__ = 'xhb'

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, func
import os


class MyDict(dict):
    def __init__(self, dictobj={}):
        super(MyDict, self).__init__()

    def __getattr__(self, name):
        # Pickle is trying to get state from your object, and dict doesn't implement it.
        # Your __getattr__ is being called with "__getstate__" to find that magic method,
        # and returning None instead of raising AttributeError as it should.
        if name.startswith('__'):
            raise AttributeError
        return self.get(name)

    def __setattr__(self, name, val):
        self[name] = val

    def __hash__(self):
        return id(self)


class Model():

    DATABASE_URL = os.environ.get('DATABASE_URL')

    def __init__(self, db_url=None, **kwargs):
        self.db_url = db_url or self.DATABASE_URL
        if not self.db_url:
            raise ValueError('You must provide a db_url.')

        self._engine = create_engine(self.db_url, **kwargs)
        self.metadata = MetaData()
        self.tab = {}

    def tables(self, only=None):
        self.metadata.reflect(self._engine, only=only)
        Base = automap_base(metadata=self.metadata)
        Base.prepare()
        for k, v in Base.classes.items():
            self.tab[k] = v

    def session(self):
        return Session(self._engine)


if __name__ == "__main__":
    mod = Model("mysql+pymysql://wdp:123456@127.0.0.1:3306/tt?charset=utf8",
                pool_size=10,
                pool_recycle=1600,
                pool_pre_ping=True,
                pool_use_lifo=True,
                echo_pool=True,
                max_overflow=5
                )
    a = mod.tables(["user_info"])

    user = mod.tab["user_info"]

    b = mod.tables(['order_info'])
    order = mod.tab["order_info"]

    session = mod.session()

    user_prices = session.query(user.userid, func.sum(order.prince)).join(
        order, user.userid == order.userid).group_by(user.userid).all()

    print(user_prices)



