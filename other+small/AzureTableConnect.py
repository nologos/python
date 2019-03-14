# https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python

import azure
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


table_service = TableService(account_name='downloaderstoragetables', account_key='u2QfPKgaSBPZmRBSkbfJw71vw8ar4pJPB8aoFgS+san0q/7vcPGttPRvGtt1wgustB6Ui2pe0Ffs+32l1eDDYQ==')


# table_service.create_table('testtwo')

task = {'PartitionKey': 'asmongold', 'RowKey': 'another one , videotitle should go here', 'binarytest': 110000101001011, 'description' : 'have this field as generic description', 'priorityORrandomint' : 3030}
table_service.insert_or_merge_entity('downloadednew', task)

