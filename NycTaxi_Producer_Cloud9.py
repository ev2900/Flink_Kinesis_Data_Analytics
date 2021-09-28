# Download the taxi cab file
'''
	wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv
'''

# Install boto3
'''
	pip install boto3
'''

# Import req. libraries
import json
import csv
import boto3

# Make JSON from the yellow cab trip data CSV files
taxiCabRides = []

with open('./yellow_tripdata_2020-01.csv', encoding='utf-8') as csvf:
	csvReader = csv.DictReader(csvf)
         
	for rows in csvReader:
		taxiCabRides.append(rows)
		# print(rows)

# print(taxiCabRides[0])

# Create a kinesis client
client = boto3.client('kinesis')

counter = 0

for ride in taxiCabRides:

	# print(ride)
	# print(json.dumps(ride))
	# print(ride['VendorID'])

	# Send message to Kinesis DataStream
	response = client.put_record(
		StreamName = "yellow-cab-trip",
		Data = json.dumps(ride),
		PartitionKey = str(hash(ride['tpep_pickup_datetime']))
	)

	counter = counter + 1

	print('Message sent #' + str(counter))
	
	# If the message was not sucssfully sent print an error message
	if response['ResponseMetadata']['HTTPStatusCode'] != 200:
		print('Error!')
		print(response)