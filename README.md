# Kinesis Data Analytics Lab

Processing real-time data via. Kinesis Data Analytics - Apache Flink

Youtube video(s)
1.    [Send Data to Kinesis from a Python Script][12]
2.    Optional - [Send Data to Kinesis from a KDA Notebook][22]
3.    [Create a Kinesis Data Analytics Studio and Upload a Notebook][13]
4.    [Running the Interactive Flink Zeppelin Notebook][16]
5.    [Deploy a Kinesis Data Analytics Studio Notebook][21]

## Data Producer

***Note*** if you want to get started and do not want to set up a Kinesis Data Stream & load data into the stream / set up a [data simulator][19], use the [sql_1.13_DataGen.zpln][18] notebook. This Zeppelin notebook uses the Flink [DataGen][17] connector to generate data with in the Zeppelin notebook **without needing a connnection to Kineis or Kafka**.

In order to get started with Apache Flink via. Kinesis Data Analytics (KDA), a Kinesis Data Stream with sample data is required. The [```kinesis_data_producer```][1] folder provides two python scripts that will read the data from the CSV file [```yellow_tripdata_2020-01.csv```][3] in the [```data```][2] folder and stream each line in the file as a JSON record/message to a Kineis Data Stream specified.

Two variations of this python data producer are provided.
* [```NycTaxi_Producer_Cloud9_JSON.py```][4]
* [```NycTaxi_Producer_Desktop_JSON.py```][5]

The two scripts/programs are very similar. A few differences exist depending on if you want run the producer application(s) from your local computer/laptop or if you want to use  [Cloud9][6].

For a step by step walk through view the Youtube video [Send Data to Kinesis from a Python Script][12] 

**An alternative method to send sample data to a Kinesis Data Stream - without the need to set up the python data producer**(s) described above - is to use the [```Nyc_Taxi_Produce_KDA_Zeppelin_Notebook.zpln```][20] notebook in KDA Studio. This notebook can be uploaded and has instructions to sends sample data from S3 to a Kinesis Data Stream.

To benefit the most from the sample Flink code / labs provided it will be important that you can easily start and stop a python data producer. 

## Interactive KDA Flink Zeppelin Notebook(s) 

The [```interactive_KDA_flink_zeppelin_notebook```][7] folder provides [Zeppelin][8] notebooks that are design to work with [Kinesis Data Analytics Studio][9]. Deploy a Kinesis Data Analytics Studio instance and upload the Zeppelin (.zpln) notebook(s). 

Note - with in the the [```interactive_KDA_flink_zeppelin_notebook```][7] folder are subfolders 
* [```Flink v1.11```][10]
* [```Flink v1.13```][11]

Depending on which version of Flink your notebook is configured to use. I would recommend using Flink v1.13.

To upload the notebook

<img width="795" alt="upload_notebook" src="https://user-images.githubusercontent.com/5414004/137349377-80cc961e-e918-4c31-85c5-bfaac7bf3da9.png">

Once uploaded and opended in Zeppelin. Run the notebook one cell at a time

<img width="788" alt="interactive_notebook" src="https://user-images.githubusercontent.com/5414004/137350050-c962e127-f198-4819-9e2a-55dfc16571ed.PNG">

For a step by step walk through of the notebook running view the Youtube video [Running the Interactive Flink Zeppelin Notebook][16]

## Deployable KDA Flink Zeppelin Notebook(s)

Kinesis Data Analytics Studio provides an excellent development environment. When you are ready to deploy you application Kinesis Data Analytics Studio has a mechanism to build and deploy your notebook code as a long running Kinesis Data Analytics application. 

To deploy your notebook 

Ensure that when you created your notebook environment you configured the ```Deploy as application configuration - optional``` setting with a valid S3 bucket.

<img width="614" alt="deploy_config" src="https://user-images.githubusercontent.com/5414004/137352921-d16fc081-4190-4e42-b978-26b247139f86.png">

To access this configuration menu during the creation of your studio notebook select ```Create with custom settings``` instead of the default Quick create with sample code. Follow the set up prompts and on ```Step 3 - Configure``` select an S3 bucket for the ```Deploy as application configuration - optional```

With this configured your Zeppelin notebook select ```Build deployable and export to Amazon S3``` 

<img width="783" alt="build_action" src="https://user-images.githubusercontent.com/5414004/137355086-2317d761-0d75-444f-af90-0a4a042b575c.png">

Once the build is complete. Select ```Deploy deployable as Kinesis Analytics application``` 

<img width="782" alt="deploy_action" src="https://user-images.githubusercontent.com/5414004/137355601-e8c495d2-ea88-4420-b21f-6f3e95801a7d.png">

When the deployment is complete you will see the application under the analytics application section of Kinesis Data Analytics 

<img width="739" alt="deployed" src="https://user-images.githubusercontent.com/5414004/137364432-45a2fa75-09bf-4c28-82e0-d007c6cd66b7.png">

## Future Improvements Planned for this Repository
* YouTube video - DataGen based interactive_KDA_flink_zeppelin_notebook [sql_1.13_DataGen.zpln][18]
* [Versioned Tables][15]
* Examples for Managed Streaming for Kafka (MSK)

[1]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/kinesis_data_producer
[2]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/data
[3]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/data/yellow_tripdata_2020-01.csv
[4]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Cloud9_JSON.py
[5]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Desktop_JSON.py
[6]:https://aws.amazon.com/cloud9/
[7]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zeppelin_notebook
[8]:https://flink.apache.org/news/2020/06/15/flink-on-zeppelin-part1.html
[9]:https://aws.amazon.com/blogs/aws/introducing-amazon-kinesis-data-analytics-studio-quickly-interact-with-streaming-data-using-sql-python-or-scala/
[10]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zeppelin_notebook/Flink%20v1.11
[11]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zeppelin_notebook/Flink%20v1.13
[12]:https://www.youtube.com/watch?v=pPCg6SWhv-0
[13]:https://www.youtube.com/watch?v=5--oWB2udCc
[14]:https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/raw/
[15]:https://nightlies.apache.org/flink/flink-docs-release-1.13/docs/dev/table/concepts/versioned_tables/
[16]:https://youtu.be/dO9GFcAy-YM
[17]:https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/datagen/
[18]:https://github.com/ev2900/Flink_Kinesis_Data_Analytics/blob/main/interactive_KDA_flink_zeppelin_notebook/Flink%20v1.13/sql_1.13_DataGen.zpln
[19]:https://github.com/ev2900/Flink_Kinesis_Data_Analytics/tree/main/kinesis_data_producer
[20]:https://github.com/ev2900/Flink_Kinesis_Data_Analytics/blob/main/kinesis_data_producer/Nyc_Taxi_Produce_KDA_Zeppelin_Notebook.zpln
[21]:https://youtu.be/0GO8drcWv3c
[22]:https://youtu.be/oAQO8cmip7Q
