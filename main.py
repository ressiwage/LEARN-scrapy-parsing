import sqlite3, time, json, schedule
from multiprocessing import Process
from twisted.internet import reactor
import multiprocessing, datetime, shutil

conn = sqlite3.connect('data.db')
cursor = conn.cursor()


from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy import cmdline 
from quant.quant.spiders.quantspider import Spider
import schedule, time
from twisted.internet import reactor


def get_data():
    a = open('obtained.json','w+')
    a.close()
    process = CrawlerProcess({'FEED_FORMAT': 'json','FEED_URI': 'obtained.json'})
    process.crawl(Spider)
    process.start()
    return None


      
if __name__ == '__main__':
    while True:
        p = multiprocessing.Process(target=get_data)
        p.start()
        p.join()
        
        time.sleep(1)

        import sys
        del sys.modules['twisted.internet.reactor']
        from twisted.internet import reactor
        from twisted.internet import default
        default.install()       

        
        try:
            print(type(json.load(open('obtained.json', 'r', encoding='utf8'))))
        except json.decoder.JSONDecodeError as e:
            print(e)
            continue
        
        records = [i for i in cursor.execute("SELECT * FROM news").fetchall()]
        print(records)
        for record in json.load(open('obtained.json', 'r', encoding='utf8')):
            if record['name'] not in [i[0] for i in records]:
                query = rf"""INSERT INTO news(title, body, creation) VALUES(?,?,?)"""
                values=(record['name'], record['body'], datetime.datetime.now())
                cursor.execute(query, values)
                conn.commit()

        try:
            shutil.copy('data.db', 'data_replicated.db')
        except:
            pass