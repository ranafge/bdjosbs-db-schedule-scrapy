# from _typeshed import Self
import scrapy
import json
from ..items import BdjobscircularItem
from itemloaders import ItemLoader


class ExampleSpider(scrapy.Spider):
    name = 'bdjobs'
    allowed_domains = ['bdjobs.com']

    cookies = {'JOBSRPP': '100',
                'TR': '',
                'JM': '',
                'EM': '',
                'CV': '',
                'ASPSESSIONIDSUBCCQCT': 'PPCAPKLBGMOIGAOLNIIAHNGH',
                'JOBSBRWWIDTH': '780',
                '__oagr': 'true',
                '_ga_DZMZ7HXHJ2': 'GS1.1.1638637922.1.0.1638637922.0',
                '_ga': 'GA1.2.1253729954.1638637923',
                '_gid': 'GA1.2.105823524.1638637924',
                '_gat_gtag_UA_36961161_4': '1',
                '__gads': 'ID=4688441543612e41-22e531f65bcf00ac:T=1638637923:S=ALNI_MYD4lQoEiQEndKd1EJTLkVSz_Hp8Q',
                'lses': '1.aTos8VaK3UMdFUvF8AFwbHFNf5d6oZ0Y'
                }

    data  = {'joblisting_common_init.asp?fcatId': '-1',
                'locationId': '',
                'iCat': '0',
                'JobType': '0',
                'JobLevel': '0',
                'JobPosting': '0',
                'JobDeadline': '0',
                'JobKeyword': 'python',
                'ListOrder': "''",
                'Exp': '0',
                'Age': '0',
                'Gender': '',
                'GenderB': '',
                'MDate': '',
                'ver': '',
                'OrgType': '0',
                'news': '0',
                'RetiredArmy': '',
                'Workstation': '',
                'pwd': '',
                'AccessibilityAware': ''
                }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Origin': 'https://jobs.bdjobs.com',
                'Connection': 'keep-alive',
                'Referer': 'https://jobs.bdjobs.com/jobsearch.asp',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers'
                }


    

    def start_requests(self):
        yield scrapy.FormRequest('https://jobs.bdjobs.com/joblisting_common_init.asp?fcatId=-1&locationId=&iCat=0&Job\
                Type=0&JobLevel=0&JobPosting=0&JobDeadline=0&JobKeyword=python&Gender=&GenderB=&MDate=&ver=&OrgType=0&news=0&R\
                etiredArmy=&Workstation=&pwd=&AccessibilityAware=', method='POST', headers=self.headers, cookies=self.cookies, body=json.dumps(self.data),
                callback=self.parse
                )
        


    def parse(self, response):
        for data in (response.css('div.col-sm-9.col-sm-pull-9')):
            item = BdjobscircularItem()
   
            item['jobTitle'] = ''.join(data.css('div.job-title-text a::text').getall()).strip()
            item["jobDetailsLink"] = 'https://jobs.bdjobs.com/'+data.css('div.job-title-text a::attr(href)').get()
            item["companyName"] = ''.join(data.css('div.comp-name-text::text').getall()).strip()
            yield item
       
