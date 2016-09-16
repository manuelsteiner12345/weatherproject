import pyodbc
from twython import TwythonStreamer
import json
import time

cnx = pyodbc.connect('DSN=hi')
cursor = cnx.cursor()
tweets = []
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        tweets.append(data)
        cursor.execute("insert into dbo.twitter2 (tweet, time) values (?, getdate())", json.dumps(data))
        cnx.commit()

        # for t in tweets:

        if data['lang'] == 'en':
            print 'received tweet #', len(tweets)

        if len(tweets) > 100000000000000000000000000000000:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

stream = MyStreamer('82NxMfwqwGQWRcG7vYICpFxBz', 'EsEP0fkEXby3D6gEJkbxeO59ZF5tqnHEKUBCNAh004TwD1dyWG', '77536475147182899'
                                                                                                     '2-lP56lYTHk5Q3Lzl'
                                                                                                     'vYkJxAdOx7QMIzbd',
                  'MGSb64bUWkW1xmELCaRQ3p1VpoENmqbeRwmtlBfuU8I9X')
stream.statuses.filter(track='london temperature')

# row = cursor.fetchall()
# rl = list(row)
# for r in rl:
#     print r



