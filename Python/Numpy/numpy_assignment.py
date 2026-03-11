import logging
import pandas as pd


#TASK0
# Create logger
logger = logging.getLogger(__name__)  # Use module name
logger.setLevel(logging.DEBUG)

# Create format
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logging
logger.info("Start the pipeline")




#TASK1
record=pd.read_csv('employees.csv')
logger.info(f"The number of records in the file are:{len(record)} and the schema details are as follow: {record.dtypes} ")




#TASK2
logger.info(f"Missing Values across the following columns are:{record.isna().sum()}")


if 'Age' in record.columns:
    median_age= record['Age'].median()
    record["Age"]=record["Age"].fillna(median_age)
    logger.info(f"The missing value in age were replaced with the median of: {median_age}")

if 'Salary' in record.columns:
    mean_salary= record['Salary'].mean()
    record["Salary"]=record["Salary"].fillna(mean_salary)
    logger.info(f"The missing value in Salary were replaced with the mean of: {mean_salary}")


# Remove duplicate records based on Employee_ID
if 'Employee_ID' in record.columns:
    before_duplicates = len(record)
    record.drop_duplicates(subset='Employee_ID', keep='first', inplace=True)
    after_duplicates = len(record)
    removed_count = before_duplicates - after_duplicates
    logger.info(f"Removed {removed_count} duplicate records based on Employee_ID")

 #Standardize column names for consistency
original_columns = record.columns.tolist()

#lowercase and replace spaces with underscores
record.columns = [col.strip().lower().replace(" ", "_") for col in record.columns]
logger.info(f"Columns renamed from {original_columns} to {record.columns.tolist()}")

# Datatype Conversion
if 'age' in record.columns:
    record['age'] = record['age'].astype(int)
    logger.info("Converted 'age' column to integer type")
if 'salary' in record.columns:
    record['salary'] = record['salary'].astype(float)
    logger.info("Converted 'salary' column to float type")
if 'employee_id' in record.columns:
    record['employee_id'] = record['employee_id'].astype(str)
    logger.info("Converted 'employee_id' column to string type")
if 'joining_date' in record.columns:
    record['joining_date'] = pd.to_datetime(record['joining_date'],format='mixed')
    logger.info("Converted 'joining_date' column to date type")    

logger.info(f"Final dataset shape: {record.shape}")
logger.info(f"Final missing values check: {record.isna().sum()}")
logger.info(f"Final data type checking:{record.dtypes}")




#TASK3
before_filter = len(record)
logger.info(f"Number of records before filtering: {before_filter}")

#Filtered based on the Requirements
filtered_record = record[
    ((record['age'] > 25) | (record['salary'] > 40000)) &
    (record['resigned'] != 'False')
]

#New coloumn added
today = pd.Timestamp.today()
filtered_record['yearsincompany'] = (
    (today - filtered_record['joining_date']).dt.days // 365
)

logger.info("Created column 'yearsincompany'")

after_filter = len(filtered_record)

logger.info(f"Number of records after filtering: {after_filter}")
logger.info(f"Number of records removed during filtering: {before_filter - after_filter}")





#TASK4:
# Department level aggregation
dept_stats = filtered_record.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    median_age=('age', 'median')
)

logger.info(f"Department level statistics:\n{dept_stats}")


# Salary increment
dept_name = "Finance"
filtered_record.loc[
    filtered_record['department'] == dept_name,
    'salary'
] *= 1.10

updated_count = (filtered_record['department'] == dept_name).sum()


logger.info(f"Applied 10% salary increment to department: {dept_name}")
logger.info(f"Employees affected: {updated_count}")



#TASK5
#Sorted by Joining Date
filtered_record = filtered_record.sort_values(
    by='joining_date',
    ascending=False
)

logger.info("Data sorted by joining_date in descending order")

#Exported as json object file
filtered_record.to_json(
    'cleaned_employees.json',
    orient='records',
    date_format='iso',
    indent=2
)

final_count = len(filtered_record)

logger.info(f"Final dataset exported successfully to cleaned_employees.json")
logger.info(f"Total records exported: {final_count}")