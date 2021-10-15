import json
import csv
import boto3

# Set up
'''

	1. Run 'pip install boto3' if you have not already
	2. Install aws CLI - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
	3. Run 'aws configure'

'''

# Make JSON from the yellow cab trip data CSV files
taxiCabRides = []

with open('../data/yellow_tripdata_2020-01.csv', encoding='utf-8') as csvf:
	csvReader = csv.DictReader(csvf)
         
	for rows in csvReader:
		taxiCabRides.append(rows)
		# print(rows)

# print(taxiCabRides[0])

# Sample JSON record
'''
{
	'VendorID': '1',
	'tpep_pickup_datetime': '2020-01-01 00:28:15',
	'tpep_dropoff_datetime': '2020-01-01 00:33:03',
	'passenger_count': '1',
	'trip_distance': '1.20',
	'RatecodeID': '1',
	'store_and_fwd_flag': 'N',
	'PULocationID': '238',
	'DOLocationID': '239',
	'payment_type': '1',
	'fare_amount': '6',
	'extra': '3',
	'mta_tax': '0.5',
	'tip_amount': '1.47',
	'tolls_amount': '0',
	'improvement_surcharge': '0.3',
	'total_amount': '11.27',
	'congestion_surcharge': '2.5'
}
'''

# Create a kinesis client
client = boto3.client('kinesis')

counter = 0

for ride in taxiCabRides:

	# print(ride)
	# print(json.dumps(ride))
	# print(ride['VendorID'])
	# print(ride['tpep_pickup_datetime'])

	# Send message to Kinesis DataStream
	response = client.put_record(
		StreamName = "yellow-cab-trip",
		Data = json.dumps(ride),
		PartitionKey = str(hash(ride['tpep_pickup_datetime']))
	)

	counter = counter + 1

	print('Message sent #' + str(counter))
	
	# print(response)

	# If the message was not sucssfully sent print an error message
	if response['ResponseMetadata']['HTTPStatusCode'] != 200:
		print('Error!')
		print(response)