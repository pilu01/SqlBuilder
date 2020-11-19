# @Time    : 2020/11/18 下午8:47

__author__ = 'xhb'


from sql_constants import SqlConstants
import sqlalchemy


class SqlBuilder(SqlConstants):
    sql_constants = SqlConstants

    def build_select(self, str_table_name, dic_data, boo_format_data=True):
        """
        读取一组数据
        @params str_table_name string 表名
        @params str_type string 类型，可以是list, first
        @prams dic_data dict 数据字典
        @params booformat_data bool 是否格式化数据，默认为True
        """
        if boo_format_data:
            dic_data = self.formate_data(dic_data)

        str_table_name = self.build_table_name(str_table_name)
        str_fields = self.build_fields(dic_data[SqlConstants.FIELDS])
        str_condition = self.build_condition(dic_data[SqlConstants.CONDITION])
        str_join = ''

        for join_item in dic_data[SqlConstants.JOIN]:
            str_join += self.build_join(join_item)

        str_order = self.build_order(dic_data[SqlConstants.ORDER])
        str_group_by = self.build_group_by(dic_data[SqlConstants.GROUP_BY])

        str_sql = "select %s from %s %s %s %s %s" % (
            str_fields, str_table_name, str_join, str_condition, str_group_by, str_order)

        return str_sql



    def build_table_name(self, str_table_name):
        """ 构建表名
        """
        return str_table_name

    def build_fields(self, fields):
        if isinstance(fields, list):
            fields_str = ", ".join(fields)
        elif isinstance(fields, str):
            fields_str = fields
        else:
            raise TypeError("fields 需要为 str or list")

        return fields_str if fields_str != "" else " * "

    def build_join(self, str_join):
        s = """
        left join {}
        on ({})
        """.format(str_join.get(SqlConstants.TABLE_NAME, ''),
                   str_join.get(SqlConstants.JOIN_CONDITION, ''))

        return s

    def build_condition(self, str_condition):
        """ 构建条件
        @params dicCondition dict 条件字典
        """
        return 'where %s' % str_condition if str_condition else ''

    def build_group_by(self, str_group_by):
        """
        分组条件
        """
        return 'group by %s' % str_group_by if str_group_by else ''

    def build_having(self, str_having):
        return 'having %s' % str_having if str_having else ''

    def build_limit(self, lisLimit):
        pass

    def build_order(self, str_order):
        """ 构建order
        """
        return 'order by ' + str_order if str_order else ''

    def formate_data(self, dic_data):
        """格式化数据
        将fields, condition, join 等数据格式化返回
        @params dic_data dict 数据字典
        """
        # fields
        dic_data[SqlConstants.FIELDS] = dic_data.get(SqlConstants.FIELDS, '')

        # join
        dic_data[SqlConstants.JOIN] = dic_data.get(SqlConstants.JOIN, [])

        # conditon
        dic_data[SqlConstants.CONDITION] = dic_data.get(SqlConstants.CONDITION, '')

        # order
        dic_data[SqlConstants.ORDER] = dic_data.get(SqlConstants.ORDER, '')

        # group_by
        dic_data[SqlConstants.GROUP_BY] = dic_data.get(SqlConstants.GROUP_BY, '')

        # having
        dic_data[SqlConstants.HAVING] = dic_data.get(SqlConstants.HAVING, '')

        # limit
        dic_data[SqlConstants.LIMIT] = dic_data.get(SqlConstants.LIMIT, '')

        if SqlConstants.KEY in dic_data:
            if isinstance(dic_data[SqlConstants.KEY], str):
                dic_data[SqlConstants.KEY] = dic_data[SqlConstants.KEY].split(',')
            val_list = []
            for i in dic_data[SqlConstants.KEY]:
                val_list.append(':{}'.format(i))
            # val
            dic_data[SqlConstants.VAL] = ','.join(val_list)
            # key
            dic_data[SqlConstants.KEY] = ','.join(dic_data[SqlConstants.KEY])

        return dic_data









if __name__ == '__main__':
    """
    以oracle 改造
    """
    sql = "select * from tt.order_info where orderid =1"
    sql1 = "select orderid, paidtime from tt.order_info where userid = 11211 and prince =833"
    sql2 = """
        select userid , count(*) cn 
        from tt.order_info 
        group by userid
        order by count(*) desc
        """

    dic_data = {
        SqlConstants.FIELDS: ['jlbh', 'jjbh'],
        SqlConstants.TABLE_NAME: 'AJ_JBXX',
        SqlConstants.CONDITION: "jjbh = 32050000000011019962"
    }

    s = SqlBuilder()
    print(s.build_select("AJ_JBXX", dic_data))


