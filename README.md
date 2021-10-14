# Kinesis Data Analytics Lab

Processing real-time data via. Kinesis Data Analytics - Apache Flink.

## Data Producer
In order to get started with Apache Flink via. Kinesis Data Analytics (KDA). A Kinesis Data Stream with sample data is required. The [```kinesis_data_producer```][1] folder provides two python scripts that will read the data from the CSV file [```yellow_tripdata_2020-01.csv```][3] in the [```data```][2] folder and stream each line in the file as a JSON record/message to a Kineis Data Stream specified.

Two variations of this python data producer are provided.
* [```NycTaxi_Producer_Cloud9_JSON.py```][4]
* [```NycTaxi_Producer_Desktop_JSON.py```][5]

The two scripts/programs are very similar. A few differences exist depending on if you want run the producer application(s) from your local computer/laptop or if you want to use  [Cloud9][6].

To benifit the most from the sample(s) Flink code / labs provided it will be important that you can easily start and stop a python data producer. 

## Interactive KDA Flink Zeppelin Notebook(s)

The [```interactive_KDA_flink_zepline_notebook```][7] folder provides [Zeppelin][8] notebooks that are design to work with [Kinesis Data Analytics Studio][9]. Deploy a Kinesis Data Analytics Studio instance and upload the Zeppelin (.zpln) notebook(s). 

Note - with in the the [```interactive_KDA_flink_zepline_notebook```][7] folder are subfolders 
* [```Flink v1.11```][10]
* [```Flink v1.13```][11]

Depending on which version of Flink your notebook is configured to use. I would recommend using Flink v1.13.

To upload the notebook

<img width="795" alt="upload_notebook" src="https://user-images.githubusercontent.com/5414004/137349377-80cc961e-e918-4c31-85c5-bfaac7bf3da9.png">

Once uploaded and opended in Zeppelin. Run the notebook one cell at a time

<img width="788" alt="interactive_notebook" src="https://user-images.githubusercontent.com/5414004/137350050-c962e127-f198-4819-9e2a-55dfc16571ed.PNG">

## Deployable KDA Flink Zeppelin Notebook(s)

Kinesis Data Analytics Studio provides an excellent development environment. When you are ready to deploy you application Kinesis Data Analytics Studio has a mechanism to build and deploy your notebook code as a long running Kinesis Data Analytics application. 

To deploy your notebook 

Ensure that when you created your notebook enviorment you configured the ```Deploy as application configuration - optional``` setting with a valid S3 bucket.

<img width="614" alt="deploy_config" src="https://user-images.githubusercontent.com/5414004/137352921-d16fc081-4190-4e42-b978-26b247139f86.png">

To access this configuration menu during the creation of your studio notebook select ```Create with custom settings``` instead of the default Quick create with sample code. Follow the set up prompts and on ```Step 3 - Configure``` select an S3 bucket for the ```Deploy as application configuration - optional```

With this configured your Zeppelin notebook select ```Build deployable and export to Amazon S3``` 

<img width="783" alt="build_action" src="https://user-images.githubusercontent.com/5414004/137355086-2317d761-0d75-444f-af90-0a4a042b575c.png">

Once the build is complete. Select ```Deploy deployable as Kinesis Analytics application``` 

<img width="782" alt="deploy_action" src="https://user-images.githubusercontent.com/5414004/137355601-e8c495d2-ea88-4420-b21f-6f3e95801a7d.png">

When the deployment is complete you will see 

[1]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/kinesis_data_producer
[2]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/tree/main/data
[3]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/data/yellow_tripdata_2020-01.csv
[4]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Cloud9_JSON.py
[5]:https://github.com/ev2900/Kinesis_Data_Analytics_Lab/blob/main/kinesis_data_producer/NycTaxi_Producer_Desktop_JSON.py
[6]:https://aws.amazon.com/cloud9/
[7]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zepline_notebook
[8]:https://flink.apache.org/news/2020/06/15/flink-on-zeppelin-part1.html
[9]:https://aws.amazon.com/blogs/aws/introducing-amazon-kinesis-data-analytics-studio-quickly-interact-with-streaming-data-using-sql-python-or-scala/
[10]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zepline_notebook/Flink%20v1.11
[11]:https://github.com/ev2900/Apache_Flink_via_Kinesis_Data_Analytics/tree/main/interactive_KDA_flink_zepline_notebook/Flink%20v1.13
