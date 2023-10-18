# Fast Food Knowledge Mapping Database

This repository contains code for the "Design of a Database for Knowledge Management in Fast Food" project. The project aims to simulate a database for knowledge management in the fast-food industry, specifically focusing on delivery platforms, and to visualize relevant statistics using Python.

## Prerequisites

Before running the code, make sure you have the following prerequisites:

- Python (3.6 or higher)
- MySQL server
- Required Python packages (install using `pip`):
  - `mysql-connector-python`
  - `matplotlib`
  - `pandas`

## Configuration

Make sure to configure your MySQL connection in the `config` dictionary within the `main` function. You should provide the `user`, `password`, `host`, and `database` information.

```python
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'KNOWLEDGE_MAPPING',
    'raise_on_warnings': True
}
```

## Code Structure

- `connect_to_database()`: Function to establish a connection to the MySQL database.

- `clean_and_convert_to_numeric(x)`: Function to clean and convert data to numeric values.

- `execute_query_and_plot_df(query, x_label, y_label, title, filename, config)`: Function to execute a query, plot the results using Matplotlib, and save the plot as an image.

- `main(config)`: The main function that defines and executes a series of SQL queries and plots the results.

## SQL Queries

The code includes several predefined SQL queries related to fast food knowledge management, such as:

- Average Cost
- Total Revenue for Each Restaurant
- Most Popular Menu Item
- Most Profitable Item
- Total Spent by First Name
- Number of Orders by First Name
- Average Total per Order by First Name

You can customize or extend these queries as needed for your specific knowledge management project.

## Usage

1. Configure the MySQL connection details in the `config` dictionary.

2. Run the `main(config)` function to execute the predefined queries and generate corresponding plots.

## Output

The code will generate bar plots for the executed queries and save them as image files (e.g., `query_00.png`, `query_01.png`, etc.) in the current working directory.
