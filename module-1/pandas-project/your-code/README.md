# PANDAS PROJECT
# Demonstration of Data Cleaning and Manipulation with Pandas


The Ironhack team has proposed the development of a project where a database obtained from open resources in the web will be cleaned, manipulated and analyzed. The database chosen for the current exercise is "Gun Violence Data" coming from the GitHub repository :

[https://github.com/jamesqo/gun-violence-data](https://github.com/jamesqo/gun-violence-data)

Such repository has been found through [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)



# Analysis of the Gun Violence data

The chosen database contains all records of crimes in the USA from 2013 to 2018 where at least one gun was involved. The database is composed of a unique table that will become our dataset. Information within the dataset is large and consistent enough to allow extracting conclusions from the data.

# Preparing the environment and importing the dataset

```
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
```



