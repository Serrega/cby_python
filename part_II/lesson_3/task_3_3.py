import mysql.connector as sql
import mysql.connector.errors


class BaseOperate:
    def __init__(self):
        self.tablename = 'product'
        self.mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='gurri',
            database='first'
        )
        self.mycursor = self.base_connect()
        self.delete_str()
        self.update_str()
        self.new_str()
        self.new_column()
        self.print_table()

    def base_connect(self):
        return self.mydb.cursor()

    def delete_str(self):
        self.mycursor.execute(f'delete from {self.tablename} where id=2')
        self.mydb.commit()

    def update_str(self):
        self.mycursor.execute(f'update {self.tablename} set price="63 руб" where name="молоко"')
        self.mycursor.execute(f'update {self.tablename} set price="34 руб" where name="макароны"')
        self.mydb.commit()

    def new_str(self):
        self.mycursor.execute(f'insert into {self.tablename} (name, price) values ("мука ржаная", "54 руб")')
        self.mydb.commit()

    def new_column(self):
        self.mycursor.execute(f'ALTER TABLE {self.tablename} ADD COLUMN note VARCHAR(255) AFTER price')
        self.mydb.commit()

    def print_table(self):
        self.mycursor.execute(f'select * from {self.tablename}')
        print(*self.mycursor.fetchall(), sep='\n')


if __name__ == '__main__':
    BaseOperate()
