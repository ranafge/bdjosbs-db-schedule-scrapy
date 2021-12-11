import  schedule
import time
import os

print('\nScheduler initialied\n')

schedule.every(2).minutes.do(lambda : os.system('scrapy crawl bdjobs'))
print('Next job is set ot run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(2)
