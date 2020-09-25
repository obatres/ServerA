import pymongo


client = pymongo.MongoClient("mongodb://admin:admin@clusterservera-shard-00-00.zcacd.gcp.mongodb.net:27017,clusterservera-shard-00-01.zcacd.gcp.mongodb.net:27017,clusterservera-shard-00-02.zcacd.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-hjvcfy-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client["ServerA"]
mycol = mydb["Datos"]

for x in mycol.find():
  print(x) 