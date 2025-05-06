import pandas as pd
pd. 

# 1. Create
# 1.1 Create from a CSV

df = pd.read_csv('telco_churn.csv') 


# 1.2 Create from a Dictionary
tempdict = {'coll' : [1,2,3], 'col2' :[4,5,6], 'col3':[7,8,9]}
dictdf = pd.DataFrame.from_dict(tempdict)


# 2. Read
# 2.1 Show Top 5 and Bottom 5 Rows

#Allows you to view top 10 rows
df.head(10)

dictdf.head()

#Allows to view bottom 15 rows
fd.tail(15)

#2.2 Show Columns and Data Type

#Allows you to view all the colmuns you have
df.columns

#Allows you to take a look at different data types that are available
df.dtypes

# 2.3 Summary Statistics

#Calculates count, mean, standard deviation, min, max, and different quartiles 
df.describe()

#Allows to calculate summmary statistics on non-float and integer values
fd.describe(include = 'object'

# 2.4 Filtering Columns \
            
df.State

#Allows you to grab a single colomn
df['International plan']

#Passes in array within the data frame 
df[['State', 'International plan']]

#Access to all unique value in data frame           
df.State.unique()

            
# 2.5 Filtering on Rows

# Grabs only the values that is wanted          
df[df['Internatinal plan'] == 'No'] 

#dual condition filer             
df[(df['Internatinal plan'] == 'No') & (df['Churn'] == False)] 

# 2.6 Indexing with iloc

 # Gets specific data wanted           
df.iloc[14]

#Allows you to get a subset of data frame
df.iloc[22:33]


# 2.7 Indexing with loc

#Copy of dataframe            
state = df.copy()

state.set_index('State', inplace=True)

state.head

state.loc['OH']

# 3. Update

# 3.1 Dropping Rows

df.isnull().sum()

#Drops rows with missing values
df.dropna(inplace=True)

# 3.2 Dropping Columns

df.drop('Area code', axis=1)

# 3.3 Creating Calculated Columns

# Creates new calculated colomn
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']


# 3.4 Updating an Entire Column
df['New Column'] = 100
df.head()

#3.5 Updating a Single Value
df.iloc[0,-1] = 10
df.head()

# 3.6 Condition based updating using apply

# 
df['Churn Binary'] = df['Churn'].apply(lambda x: l if x ==True else 0)
df[df['Churn']==True].head()
df.head()

# 4. Delete/Output

#4.1 Output to CSV

df.tocsv('output.csv')

# 4.2 Outputs to JSON
df.to_json()

# 4.3 Output to HTML

df.to_html()

#Delete a DataFrame

del df

            
