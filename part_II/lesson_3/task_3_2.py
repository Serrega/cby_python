import mysql.connector as sql
import mysql.connector.errors


class BaseCommand:
    def __init__(self):
        self.mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='gurri',
            database='first'
        )
        self.mycursor = self.base_connect()
        self.input_command()

    def base_connect(self):
        return self.mydb.cursor()

    def input_command(self):
        while (command := input('Enter SQL: ')) != 'exit':
            self.execute_command(command)
        print('Work with the database is complete')

    def execute_command(self, command: str):
        try:
            self.mycursor.execute(command)
        except mysql.connector.errors.DatabaseError as de:
            print('Database Error - ', de)
        else:
            try:
                print(*self.mycursor.fetchall(), sep='\n')
            except mysql.connector.errors.InterfaceError as ie:
                print('No result for this command - ', ie)


if __name__ == '__main__':
    BaseCommand()




