import requests
import random
import argparse
import reprlib

parser = argparse.ArgumentParser(description='Catch a web page')
parser.add_argument('url',metavar='URL',type=str,help='url of page')
parser.add_argument('-a','--all',action='store_true',help='ask for whole text')
parser.add_argument('-c','--code',dest='status_code',action='store_true',help='ask for status_code')



args = parser.parse_args()

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), )

s=requests.get(args.url, headers={'User-Agent': random.choice(USER_AGENTS)})

if args.status_code:
    print('status_code=',s.status_code)

if args.all:
    print(s.text)
else:
    print(reprlib.repr(s.text))

