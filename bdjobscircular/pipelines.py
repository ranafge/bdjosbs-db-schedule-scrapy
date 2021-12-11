import  sys
import  mysql.connector 
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json

class BdjobscircularPipeline:
    
    def __init__(self):
        self.create_conn()
        self.create_table()
    
    def create_conn(self):
        try:
            self.conn = mysql.connector.connect(
                user = 'root',
                password = 'Rana9911@',
                host = 'localhost',
                database = 'myscrapy'

            )
        except mysql.Error as e:
            print(f'Error connecting to DB platform : {e}')
            sys.exit(1)
        self.curr = self.conn.cursor()

    def create_table(self):
        # self.curr.execute("""DROP TABLE IF EXISTS bdjobs""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS bdjobs (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
            jobTitle VARCHAR(255),
            jobDetailsLink VARCHAR(255),
            companyName VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")


    # def open_spider(self, spider):
    #     self.file = open('bdjobscirculars.json', 'w')
    
    # def close_spider(self, spider):
    #     self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if 'Android' in adapter.get('jobTitle') or 'DevOps' in adapter.get('jobTitle') or 'C++' in adapter.get('jobTitle') or 'Java' in adapter.get('jobTitle')  or 'Front end' in adapter.get('jobTitle'):
            raise DropItem(f'\n\n The { item } is dropped.\n\n')
        else:
            self.store_db(item)
    
    def store_db(self, item):
        myquery = """INSERT into bdjobs(
            jobTitle, jobDetailsLink, companyName
        ) values(%s,%s,%s)
        """
        val = (
            item.get('jobTitle'),
            item.get('jobDetailsLink'),
            item.get('companyName')
        )

        self.curr.execute(myquery, val)
        self.conn.commit()
    
    def close_spider(self, item):
        self.conn.close()

        