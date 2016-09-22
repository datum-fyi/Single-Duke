import json
from pymongo import MongoClient
import pprint
    
    
client = MongoClient("mongodb://localhost:27017")

db = client.datum.single_duke

def make_pipeline():
    # complete the aggregation pipeline
    # pipeline = [{"$group" : {"_id" : "$constituencyname",
    # 						 "secondHighVotes": {"$max" : "$votes"}	
    # 						}
    # 			}			
    # 			# }, 
    #    #          {"$project" : {"followers" : "$user.followers_count", "screen_name" : "$user.screen_name", "tweets" : "$user.statuses_count"} },
    #    #          {"$sort" : {"followers" : -1} },
    #    #          {"$limit" : 1}
    #             ]
    pipeline = [
      {"$sort": {"constituencyname": 1, 'votes': -1}}, 
      {"$group": {"_id":"$constituencyname", 
                "votes": {"$push": '$votes'}
      }}
      , 
      {"$project": { 
                  "second_votes": {"$arrayElemAt": ['$votes', 1]}
       }}
      ,
      {"$sort": {"second_votes": 1}}
      ,
      {"$limit": 322}
      ,
      {"$group": {"_id":None,
      				"total_votes": {"$sum": "$second_votes"}}
      }


    ]
    return pipeline

def aggregate(db, pipeline):
    result = db.aggregate(pipeline)
    return result

pipeline = make_pipeline()
result = aggregate(db, pipeline)
pprint.pprint(result)

print(list(result))