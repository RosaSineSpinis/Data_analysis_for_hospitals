import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# write your code here
general_data = pd.read_csv('test/general.csv')
prenatal_data = pd.read_csv('test/prenatal.csv')
sports_data = pd.read_csv('test/sports.csv')

pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(general_data.head(20))
# print(prenatal_data.head(20))
# print(sports_data.head(200))

# prenatal_data.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
# sports_data.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

gen_columns = general_data.columns
prenatal_data.columns = sports_data.columns = gen_columns

df = pd.concat([general_data, prenatal_data, sports_data], ignore_index=True, axis=0)
df.drop(columns=['Unnamed: 0'], inplace=True)
# print(df.head(20))

for i, j in df.iterrows():
    if j['gender'] in ['male', 'man']:
        df.at[i, 'gender'] = 'm'
    else:
        df.at[i, 'gender'] = 'f'


df['diagnosis'].fillna(0, inplace=True)
df['blood_test'].fillna(0, inplace=True)
df['ecg'].fillna(0, inplace=True)
df['ultrasound'].fillna(0, inplace=True)
df['mri'].fillna(0, inplace=True)
df['xray'].fillna(0, inplace=True)
df['children'].fillna(0, inplace=True)
df['months'].fillna(0, inplace=True)

# print(df.head(20))

num_of_patients = {(df['hospital'] == 'general').sum(): 'general',
                   (df['hospital'] == 'prenatal').sum(): 'prenatal',
                   (df['hospital'] == 'sports').sum(): 'hospital'}

stomach_general_counter = 0
for i, j in df.iterrows():
    if j['hospital'] == 'general' and j['diagnosis'] == 'stomach':
        stomach_general_counter += 1
stomach_per_general = round(stomach_general_counter / (df['hospital'] == 'general').sum(), 3)

# dislocation_sport_counter = 0
# for i, j in df.iterrows():
#     if j['hospital'] == 'sports' and j['diagnosis'] == 'dislocation':
#         dislocation_sport_counter += 1
# dislocation_per_sport = round(dislocation_sport_counter / (df['hospital'] == 'sports').sum(), 3)

num_dislocation_per_sport = df[(df['hospital'] == 'sports') & (df['diagnosis'] == 'dislocation')].shape[0]
num_hospital_sport = df[(df['hospital'] == 'sports')].shape[0]
dislocation_per_sport = round(num_dislocation_per_sport / num_hospital_sport, 3)
# print("dislocation_per_sport", dislocation_per_sport)

median_df_general = df[(df['hospital'] == 'general')]['age'].median()
median_df_sports = df[(df['hospital'] == 'sports')]['age'].median()
diff_median = median_df_general - median_df_sports

# print(df)
# print(len(df.hospital.dropna().unique()))
# print(df.hospital.nunique())
# print(df.hospital.value_counts())
''' first question '''
df.hospital.value_counts().plot.bar()
plt.show()

''' second question '''
df.diagnosis.value_counts().plot(kind='pie')
plt.show()

''' third question '''
fig, axes = plt.subplots()
# plot violin. 'Scenario' is according to x axis,
# 'LMP' is y axis, data is your dataframe. ax - is axes instance
sns.violinplot(x='hospital', y='height', data=df, ax=axes)
axes.set_title('Violin graph')

axes.yaxis.grid(True)
axes.set_xlabel('Hospitals')
axes.set_ylabel('height')
plt.show()



#y=df.hospital.dropna().unique(), kind='bar' bins=len(df.hospital.dropna().unique()),

# print(f"The answer to the 1st question is {num_of_patients[max(num_of_patients.keys())]}")
# print(f"The answer to the 2nd question is {stomach_per_general}")
# print(f"The answer to the 3rd question is {dislocation_per_sport}")
# print(f"The answer to the 4th question is {diff_median}")
print(f"The answer to the 1st question: general")
print("The answer to the 2nd question: pregnancy")
print("The answer to the 3rd question: It's because something is wrong")
