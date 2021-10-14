# Kinesis Data Analytics Lab

Processing real-time data via. Kinesis Data Analytics - Apache Flink.

## Data Producer
In order to get started with Apache Flink via. Kinesis Data Analytics (KDA). A Kinesis Data Stream with sample data is required. The [```kinesis_data_producer```][1] folder provides two python scripts that will read the data from the CSV file [```yellow_tripdata_2020-01.csv```][3] in the [```data```][2] folder and stream each line in the file as a JSON record/message to a Kineis Data Stream specified.

Two variations of this python data producer are provided.
* [```NycTaxi_Producer_Cloud9_JSON.py```][4]
* [```NycTaxi_Producer_Desktop_JSON.py```][5]

The two scripts/programs are very similar. A few differences exist depending on if you want run the producer application(s) from your local computer/laptop or if you want to use  [Cloud9][6].

To benifit the most from the sample(s) Flink code / labs provided it will be important that you can easily start and stop a python data producer. 

## Interactive KDA Flink Zepline Notebook(s)

Under construction ... this part of the read me isn't complete yet ...

## Deployable KDA Flink Zepline Notebook(s)

Under construction ... this part of the read me isn't complete yet ...

[1]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/kinesis_data_producer
[2]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/data
[3]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/data/yellow_tripdata_2020-01.csv
[4]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Cloud9_JSON.py
[5]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Desktop_JSON.py
[6]:https://aws.amazon.com/cloud9/
