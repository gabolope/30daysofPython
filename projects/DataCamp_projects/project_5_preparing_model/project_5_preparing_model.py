# The Head Data Scientist at Training Data Ltd. has asked you to create a DataFrame called ds_jobs_transformed that stores the data in customer_train.csv much more efficiently. Specifically, they have set the following requirements:

#   Columns containing categories with only two factors must be stored as Booleans (bool).
#   Columns containing integers only must be stored as 32-bit integers (int32).
#   Columns containing floats must be stored as 16-bit floats (float16).
#   Columns containing nominal categorical data must be stored as the category data type.
#   Columns containing ordinal categorical data must be stored as ordered categories, and not mapped to numerical values, with an order that reflects the natural order of the column.
#   The DataFrame should be filtered to only contain students with 10 or more years of experience at companies with at least 1000 employees, as their recruiter base is suited to more experienced professionals at enterprise companies.

# If you call .info() or .memory_usage() methods on ds_jobs and ds_jobs_transformed after you've preprocessed it, you should notice a substantial decrease in memory usage.

import pandas as pd

ds_jobs = pd.read_csv('projects/DataCamp_projects/project_5_preparing_model/customer_train.csv')
ds_jobs_transformed = ds_jobs.copy()


#   Columns containing categories with only two factors must be stored as Booleans (bool).
print(ds_jobs_transformed.dtypes)

for name, serie in ds_jobs_transformed.items():
  if serie.nunique() == 2:
    print(f'{name} será cambiada a Boolean')
    ds_jobs_transformed[name] = ds_jobs_transformed [name].astype('category')

ds_jobs_transformed['relevant_experience'] = ds_jobs_transformed['relevant_experience'].cat.rename_categories({'Has relevant experience': True, 'No relevant experience': False})
ds_jobs_transformed['relevant_experience'] = ds_jobs_transformed['relevant_experience'].astype('bool')

ds_jobs_transformed['job_change'] = ds_jobs_transformed['job_change'].map({0.0: False, 1.0: True})
ds_jobs_transformed['job_change'] = ds_jobs_transformed['job_change'].astype('bool')



#   Columns containing integers only must be stored as 32-bit integers (int32).

for name, serie in ds_jobs_transformed.items():
  if serie.dtype == 'int64':
    print(f'{name} será cambiada a int32')
    ds_jobs_transformed[name] = ds_jobs_transformed[name].astype('int32')



#   Columns containing floats must be stored as 16-bit floats (float16).

for name, serie in ds_jobs_transformed.items():
  if serie.dtype == 'float64':
    print(f'{name} será cambiada a float16')
    ds_jobs_transformed[name] = ds_jobs_transformed[name].astype('float16')

print(ds_jobs_transformed.dtypes) 


#   Columns containing nominal categorical data must be stored as the category data type.
nominal = ['city', 'gender',  'major_discipline', 'company_type']

for name in ds_jobs_transformed.columns:
  if name in nominal:
    ds_jobs_transformed[name] = ds_jobs_transformed[name].astype('category')

print(ds_jobs_transformed.dtypes)


# Columns containing ordinal categorical data must be stored as ordered categories, and not mapped to numerical values, with an order that reflects the natural order of the column.
ordinal = ['education_level', 'enrolled_university', 'experience', 'company_size', 'last_new_job']

# Hago una función que cambia una columna a categorica ordinal
def order_ordinal(column, order_list):
  ds_jobs_transformed[column] = ds_jobs_transformed[column].astype('category')
  ds_jobs_transformed[column] = ds_jobs_transformed[column].cat.set_categories(new_categories = order_list, ordered=True)

order_ordinal('education_level', ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'])


#hago una lista con ordenada de los años de experiencia
experience_order = range(1, 21)
experience_order = [str(numero) for numero in experience_order]
experience_order.insert(0, '<1')
experience_order.insert(len(experience_order), '>20')
order_ordinal('experience', experience_order)


company_size_order = [
    '<10',
    '10-49',
    '50-99',
    '100-499',
    '500-999',
    '1000-4999',
    '5000-9999',
    '10000+'
]
order_ordinal('company_size', company_size_order)


last_new_job_order = ['never', '1', '2', '3', '4', '>4']
order_ordinal('last_new_job', last_new_job_order)

enrolled_university_order = ['no_enrollment', 'Part time course', 'Full time course']
order_ordinal('enrolled_university', enrolled_university_order)


#   The DataFrame should be filtered to only contain students with 10 or more years of experience at companies with at least 1000 employees, as their recruiter base is suited to more experienced professionals at enterprise companies.
filter1 = ds_jobs_transformed['experience'] >= '10'
filter2 = ds_jobs_transformed['company_size'] >= '1000-4999'

print('Antes', ds_jobs_transformed.size)

ds_jobs_transformed = ds_jobs_transformed.loc[filter1, :]
ds_jobs_transformed = ds_jobs_transformed.loc[filter2, :]
print('Despues', ds_jobs_transformed.size)

print('Memoria antes: ', ds_jobs.memory_usage())
print('Memoria ahora: ', ds_jobs_transformed.memory_usage())
