
# Movie Success Prediction

## Overview
The "Movie Success Prediction" project is a Python-based analytical tool designed to predict the financial success of movies. It utilizes a dataset containing movie financials to analyze the relationship between a movie's production budget and its worldwide gross revenue.

## Features
- **Data Cleaning and Preprocessing**: The script cleans the dataset by renaming columns, removing unwanted characters from monetary values, converting date formats, and dropping rows with missing or zero values.
- **Data Analysis**: It focuses on analyzing the production budget and worldwide gross revenue of movies.
- **Model Building**: The project includes a linear regression model to predict worldwide gross revenue based on the production budget.
- **Data Visualization**: It features a plot showing the relationship between production budget and worldwide gross revenue.
- **Model Evaluation**: The script evaluates the model's performance by displaying its score.

## Installation
To use this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/saeed-rhimi/movieSuccessPrediction.git
   ```
2. Navigate to the cloned repository.

3. Install the required dependencies (pandas, sklearn, matplotlib):
   ```
   pip install pandas scikit-learn matplotlib
   ```

## Usage
After installing the necessary libraries, you can run the script with the following command:
```
python main.py
```
Ensure you have the dataset 'cost-revenue-dirty.csv' in your project directory. The script will clean the data, perform the analysis, and visualize the results.

## Contributing
Contributions to this project are welcome. Please ensure to update tests as appropriate.

## License
[Specify the license or state that it's unlicensed]
