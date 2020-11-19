# @Time    : 2020/11/19 下午9:06

__author__ = 'xhb'


from sql_build import SqlBuilder
from sql_constants import SqlConstants


def equal_str(str1, str2):
    assert str1.replace('\n', '').replace(' ', '') == str2.replace('\n', '').replace(' ', ''), "sql: {} \n sql_: {}".format(str1, str2)


def test_select_sql():

    sql2 = "select id, name from user_info where id like '1%' "
    sql3 = "select id, count(*) cn from user_info group by id order by count(*) desc"
    sql4 = "select a.id, b.name from user_info a left join user_code b on a.id=b.id"


def test_sql1():
    sql1 = "select * from user_info"
    sql1_ = sb.build_select('user_info', {
        SqlConstants.FIELDS: "*",
    })

    equal_str(sql1, sql1_)


def test_sql2():
    sql1 = "select id, name from user_info where id like '1%' "
    sql1_ = sb.build_select('user_info', {
        SqlConstants.FIELDS: ['id', 'name'],
        SqlConstants.CONDITION: " id like '1%' "
    })

    equal_str(sql1, sql1_)


def test_sql3():
    sql1 = "select id, count(*) cn from user_info group by id order by count(*) desc"
    sql1_ = sb.build_select('user_info', {
        SqlConstants.FIELDS: ['id', 'count(*) cn'],
        SqlConstants.GROUP_BY: 'id',
        SqlConstants.ORDER: "count(*) desc"
    })

    equal_str(sql1, sql1_)


if __name__ == '__main__':
    sb = SqlBuilder()

    test_sql1()
    test_sql2()
    test_sql3()