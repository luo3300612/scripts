import requests
import random
from bs4 import BeautifulSoup
import reprlib
import time
import argparse

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'),)

parser = argparse.ArgumentParser(description="bilibili danmaku spyder")
parser.add_argument("-c", "--cid", type=str, help="cid of av")
parser.add_argument("-s", "--string", type=str, help="str to search")
args = parser.parse_args()


def get_page(cid, delay=0.5):
    time.sleep(delay)
    try:
        s = requests.get(f"https://api.scripts.com/x/v1/dm/list.so?oid={cid}",
                         headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=5)
    except:
        s = requests.get(f"https://comment.bilibili.com/{cid}.xml",
                         headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=5)
    if s.status_code == 200:
        s.encoding = s.apparent_encoding
        return s.text
    return False


def find_str(string, cids):
    for cid in cids:
        print(cid)
        text = get_page(cid)
        if text is False:
            print(f"cid:{cid},error")
        else:
            soup = BeautifulSoup(text, "html.parser")
            ds = soup.find_all("d")
            for d in ds:
                if string in "".join(d.contents):
                    print(d.contents)


if __name__ == "__main__":
    # print(get_page(4867928))
    find_str(args.string, [args.cid])
    # 4867928
