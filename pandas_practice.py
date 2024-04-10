#
# Devina
# Practice Pandas package
#

import pandas as pd

my_data = pd.read_csv("Data.cvs")

print(my_data)
print(my_data.info())

# Drop missing data
my_data = my_data.dropna()
print(my_data.info())

# Fix wrong format
my_data["Date"] = pd.to_datetime(my_data["Date"],format="mixed")
print(my_data)

# Fix typo
my_data.loc[7,"Duration"] = 45
print(my_data)

