# -*- coding: utf8 -*-
import sys, os, pymongo
from datetime import datetime, timedelta
from bson.objectid import ObjectId

from config import datadir

db = pymongo.MongoClient()
twitter=db.twitter
tweets=twitter.twitter

if __name__ == "__main__":
    day=datetime.strptime(sys.argv[1],"%Y-%m-%d")
    starttimestamp=day
    stoptimestamp=day+timedelta(days=1)
    start_id=hex(int(day.strftime("%s")))[2:]+"0000000000000000"
    end_id=hex(int((day+timedelta(days=1)).strftime("%s")))[2:]+"0000000000000000"
    with open(os.path.join(datadir,day.strftime("%Y-%m-%d")+".txt"),'w') as textfile:
        for tweet in tweets.find({"_id":{"$gte":ObjectId(start_id),"$lt":ObjectId(end_id)}}):
            try:
                textfile.write("\t".join([str(block) for block in [tweet["id"],tweet["text"].replace('\t',' ').replace('\r',' ').replace('\n',' '),tweet["user"]["id"],tweet["in_reply_to_user_id"],tweet["created_at"]]])+"\n")
            except Exception:
                continue