from msilib import Table
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 's7612150'
DATABASE = 'Menu'
TABLE = 'menu'

class MenuItem():
    """ 
    class that handle interaction with the dataBase allowing several actions
    """

    item_list = []
    INDEX = 0

    def __init__(self:object, item_name:str, item_price:int) -> None:
        self.item_name = item_name
        self.item_price = item_price
        MenuItem.item_list.append(self)
        MenuItem.INDEX += 1
        self.item_id = MenuItem.INDEX 
        


    @classmethod
    def exe_query(cls:object, query:str) -> None:
        """
        function that execute a query to the database and return the result
        """

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()


    def save(self:object):
        """
        create and handle a query to insert into our table in the database
        """

        query = f"insert into {TABLE} values (default, '{self.item_name}', {self.item_price});"
        self.exe_query(query)


    def update(self:object, new_name:str, new_price:int):
        """
        create and handle a query that update the value of an existing row
        """
        
        query = f" update {TABLE} set item_name = '{new_name}', item_price = {new_price} where item_id = '{self.item_id}';"
        self.exe_query(query)

        self.item_name = new_name
        self.item_price = new_price 


    def remove(self:object):
        """
        create and handle a query to delete a row in the table ( by id)
        """

        query = f"delete from {TABLE} where item_id = {self.item_id};"
        self.exe_query(query)
        MenuItem.item_list.remove(self)


item = MenuItem('Burger', 35)
# item.save()
item.update('Veggie burger', 37)
# item.remove()
print(MenuItem.item_list)