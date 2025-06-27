import pandas as pd
#Explore more regex patterns
#       Eg. The regex pattern used to validate email addresses, mobile no, string, and more
import pandas as pd

df = pd.DataFrame({'text': ['apple', 'banana', 'cherry']})
print(df[df['text'].str.contains(r'an')])

print(df[df['text'].str.contains(r'a.')])

df = pd.DataFrame({'text': ['a1', 'b2', 'c3']})
print("\n")
print(df[df['text'].str.contains(r'\d')])

print("\n")
print(df[df['text'].str.contains(r'\D')])

print("\n")
print(df[df['text'].str.contains(r'\w')])

df = pd.DataFrame({'text': ['a!', 'b@', 'c#']})
print("\n")
print(df[df['text'].str.contains(r'\W')])

df = pd.DataFrame({'text': ['a b', 'c\td', 'e\nf']})
print("\n")
print(df[df['text'].str.contains(r'\s')])

print("\n")
print(df[df['text'].str.contains(r'\S')])

# Explore more datetime function and uses in pandas

data = {
    'Date': ['2024-01-01', '2024-02-14', '2024-03-20', '2024-04-01']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Month_Name'] = df['Date'].dt.month_name()

df['Day'] = df['Date'].dt.day

df['Day_Name'] = df['Date'].dt.day_name()

df['Weekday'] = df['Date'].dt.weekday

df['Week_Number'] = df['Date'].dt.isocalendar().week

df['Quarter'] = df['Date'].dt.quarter

df['Is_Leap_Year'] = df['Date'].dt.is_leap_year

df['Day_of_Year'] = df['Date'].dt.dayofyear

df['Is_Month_End'] = df['Date'].dt.is_month_end

df['Is_Month_Start'] = df['Date'].dt.is_month_start

df['Formatted'] = df['Date'].dt.strftime('%d-%b-%Y')

print(df,"\n")



#Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output



df = pd.read_csv('trial.csv')
print("Original Data:\n", df)

df = df.drop_duplicates()

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['Name'] = df['Name'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')

print("\nCleaned Data:\n", df)

average_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
min_marks = df['Marks'].min()
top_students = df[df['Marks'] == max_marks]

print("\nAverage Marks:", average_marks)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)
print("\nTop Scoring Student(s):\n", top_students)

city_group = df.groupby('City')['Marks'].mean()
print("\nAverage Marks by City:\n", city_group)