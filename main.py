import pandas as pd

# TODO: Cleaning the dataset -------------------------------------------------
# Read the dataset
df = pd.read_csv('cost-revenue-dirty.csv')

# Rename the columns for better readability
df.columns = ['Rank', 'Release Date', 'Movie Title', 'Production Budget', 'Worldwide Gross', 'Domestic Gross']

# Remove the dollar sign and commas from the columns with monetary values
df['Production Budget'] = df['Production Budget'].str.replace('$', '').str.replace(',', '').astype(float)
df['Worldwide Gross'] = df['Worldwide Gross'].str.replace('$', '').str.replace(',', '').astype(float)
df['Domestic Gross'] = df['Domestic Gross'].str.replace('$', '').str.replace(',', '').astype(float)

# Convert the Release Date column to datetime format
df['Release Date'] = pd.to_datetime(df['Release Date'])

# Drop any rows with missing values
df.dropna(inplace=True)

# Drop any rows with a zero value
df = df[(df != 0).all(1)]

# Reset the index
df.reset_index(drop=True, inplace=True)

# Drop the unnecessary columns
df = df[['Production Budget', 'Worldwide Gross']]

# Save the cleaned dataset to a CSV file
df.to_csv('cleaned_cost_revenue_dataset.csv', index=False)

# Todo: Building Our Model -----------------------------------------------------
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)
regressor.fit(x, y)

# Todo: Visualizing Data -------------------------------------------------------
import matplotlib.pyplot as plt

plt.plot(x, regressor.predict(x), color='blue', linewidth=2)
plt.scatter(x=x, y=y, alpha=0.3, color='red')
plt.xlabel('Production Budget ($)')
plt.ylabel('Worldwide Gross ($)')
plt.title('Production Budget vs Wordwide Gross ($)')
plt.ylim(0, 3e9)
plt.xlim(0, 5e8)
plt.show()

# Todo: Evaluate Our Model -----------------------------------------------------
print(regressor.score(x, y))
