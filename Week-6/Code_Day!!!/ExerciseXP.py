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


    @classmethod
    def all(cls:object) -> list:
        """
        create and handle a query to get a list of all the data inside the database and return it
        """

        query = f"select  * from {TABLE};"
        data = cls.exe_query(query)
        return data


    @classmethod
    def get_by_name(cls:object, requested:str) -> object:
        """
        create and handle a query to get a single record(row) depending on the item_name and return it return none if not finded
        """

        query = f"select distinct item_id from {TABLE} where item_name = '{requested}';"
        
        data = cls.exe_query(query)
        if data == []:
            return None

        clean_data = int(data[0][0])
        
        return MenuItem.item_list[clean_data - 1]


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


    def delete(self:object):
        """
        create and handle a query to delete a row in the table ( by id)
        """

        query = f"delete from {TABLE} where item_id = {self.item_id};"
        self.exe_query(query)
        MenuItem.item_list.remove(self)
    
 

            

item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger', 37)
print(MenuItem.all())
print(MenuItem.get_by_name('Veggie Burger'))
