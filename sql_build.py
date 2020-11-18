# @Time    : 2020/11/18 下午8:47

__author__ = 'xhb'


from sql_constants import SqlConstants
import sqlalchemy


class SqlBuilder(SqlConstants):
    sql_constants = SqlConstants

    def build_field(self, Fields):
        str_fields = ''
        if isinstance(Fields, list):
            str_fields = ','.join(Fields)
        elif isinstance(Fields, str):
            str_fields += Fields
        else:
            str_fields = ' * '

        return str_fields

    def




if __name__ == '__main__':
    sql = "select * from tt.order_info where orderid =1"
    sql1 = "select orderid, paidtime from tt.order_info where userid = 11211 and prince =833"
    sql2 = """
        select userid , count(*) cn 
        from tt.order_info 
        group by userid
        order by count(*) desc
        """

    dic_data = {
        SqlConstants.FIELDS: ['orderid', 'paidtime'],
    }

