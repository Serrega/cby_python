import mysql.connector as sql
import mysql.connector.errors


class MyDatabase:
    def __init__(self, base_name: str, table_name: str):
        self.basename = base_name
        self.tablename = table_name
        self.mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='gurri',
        )
        self.mycursor = self.base_connect()
        self.create_base()
        self.mycursor.close()
        self.mydb.close()

    def base_connect(self):
        return self.mydb.cursor()

    def create_base(self):
        try:
            self.mycursor.execute(f'create database IF NOT EXISTS {self.basename}')
        except mysql.connector.errors.DatabaseError as de:
            print('Database Error - ', de)
        self.create_table()

    def create_table(self):
        try:
            self.mycursor.execute(f'use {self.basename}')
            self.mycursor.execute(f"create table IF NOT EXISTS {self.tablename} "
                                  f"(id int auto_increment primary key, "
                                  f"name varchar(255), "
                                  f"price varchar(255))")
        except mysql.connector.errors.DatabaseError as de:
            print('Database Error - ', de)
        self.save_data()

    def save_data(self):
        val = [('батон нарезной', '21 руб'),
               ('масло подсолнечное', '60 руб'),
               ('крупа гречневая', '80 руб'),
               ('молоко', '54 руб'),
               ('яйцо куриное', '55 руб'),
               ('кетчуп', '75 руб'),
               ('сок томатный', '92 руб'),
               ('макароны', '30 руб'),
               ('зеленый горошек', '45 руб'),
               ('селедка', '150 руб')]
        ins_tab = f"insert into {self.tablename} (name, price) values (%s, %s) " \
                  f"on duplicate key update name=values(name), price=values(price)"
        self.mycursor.executemany(ins_tab, val)
        self.mydb.commit()
        print("The database 'first' was created!")


if __name__ == '__main__':
    MyDatabase('first', 'product')




