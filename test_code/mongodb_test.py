#! /usr/bin/env python
#coding=utf-8

from pymongo import MongoClient

client = MongoClient("localhost",27017)
db_test = client['test']
doc_pytest = db_test['pytest']
print db_test.collection_names()
ger_id = doc_pytest.insert({'name':'lizy'})
print ger_id


