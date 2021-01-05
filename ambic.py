import sys
from datetime import datetime as dtm
from uuid import uuid5 as UU5, NAMESPACE_X500 as NS500

from argon2 import PasswordHasher
from bson.objectid import ObjectId
from boto3 import client as botoclient

aws_key = 'AKIAUSEAB56BQPQYGN7K'
aws_access = '/Xs2npBv096sG37dPt8nTSh7ICtIIWwVyz9Zol8R'
aws_region = 'us-west-2'

amazonclient = botoclient(
    'dynamodb',
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_access,
    region_name=aws_region
)
usr_doc = {
    'uname': 'root',
    'pwd': 'pwd_root'
}

hasher_instance = PasswordHasher()
utnow_8601 = dtm.utcnow().isoformat()
usr_doc['uid'] = UU5(NS500, usr_doc['uname'])
usr_doc['phash'] = hasher_instance.hash(usr_doc['pwd'])

collection_usr_items = {
    'users': [
        {
            'PutRequest': {
                'Item': {
                    'inscode': {'S': 'zero'},
                    'orgid': {'N': '0'},
                    'username': {'S': usr_doc['uname']},
                    'token_time': {'N': '369'},
                    'userrole': {'S': 'root'},
                    'created_stamp': {'S': utnow_8601},
                    'uid': {'S': usr_doc['uid'].hex},
                    'pwd_hash': {'S': usr_doc['phash']},
                    'document_id': {'S': str(ObjectId())},
                    'active': {'BOOL': True},
                }
            }
        }
    ]
}

response = amazonclient.batch_write_item(
    RequestItems=collection_usr_items,
    ReturnConsumedCapacity='TOTAL',
    ReturnItemCollectionMetrics='SIZE'
)

print(response)
