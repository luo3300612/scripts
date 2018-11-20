"""
元编程初级示例
下载JSON，
"""
from urllib.request import urlopen
import warnings
import os
import json
from collections import abc
import keyword  # 检查是否为关键字 str.isidentifier()检查是否为合法变量名

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


feed = load()
print(sorted(feed['Schedule'].keys()))
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        print("build")
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


myjs = FrozenJSON(feed)

print(myjs.Schedule)
