import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import re

# Function to connect to the database
def connect_to_database():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'KNOWLEDGE_MAPPING',
        'raise_on_warnings': True
    }
    return mysql.connector.connect(**config)

# Function to clean and convert data to numeric
def clean_and_convert_to_numeric(x):
    cleaned = re.sub('[^\d.]', '', str(x))
    return pd.to_numeric(cleaned, errors='coerce')

# Function to execute a query and plot the results with DataFrame
def execute_query_and_plot_df(query, x_label, y_label, title, filename, config):
    cnx = connect_to_database()
    cursor = cnx.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    cnx.close()

    if not results:
        print("No data found for the query.")
        return

    x_values = []
    y_values = []

    for result in results:
        x_values.append(result[0])  # Assumes x is the first column
        if len(result) > 1:
            y_values.append(result[1])  # Assumes y is the second column if available

    data = pd.DataFrame({x_label: x_values})

    if y_values:
        data[y_label] = y_values
        data[y_label] = data[y_label].apply(clean_and_convert_to_numeric)
        # Create the bar plot
        data.plot(x=x_label, kind='bar', legend=False)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig(filename, bbox_inches='tight')
        plt.show()
    else:
        # No y values to plot
        print("No data found for the query.")

# Main function
def main(config):
    # Define and execute queries
    queries = [
        ("Average Cost",
         "SELECT AVG(order_total) as avg_cost FROM orders JOIN restaurants ON orders.restaurant_id = restaurants.id;"),
        ("Total Revenue for Each Restaurant",
         "SELECT restaurant_name, SUM(menu_items.price * order_items.item_quantity) as total_revenue FROM order_items JOIN menu_items ON order_items.item_id = menu_items.id JOIN restaurants ON menu_items.restaurant_id = restaurants.id GROUP BY restaurant_name ORDER BY total_revenue;"),
        ("Most Popular Menu Item",
         '''
         SELECT menu_items.item_name, SUM(order_items.item_quantity) as popularity
         FROM order_items
         JOIN menu_items ON order_items.item_id = menu_items.id
         JOIN restaurants ON menu_items.restaurant_id = restaurants.id
         GROUP BY menu_items.item_name
         ORDER BY popularity DESC
         LIMIT 1;
         '''),
        ("Most Profitable Item",
         "SELECT item_name, SUM(item_quantity * menu_items.price) as total_revenue FROM order_items JOIN menu_items ON order_items.item_id = menu_items.id GROUP BY item_name ORDER BY total_revenue DESC LIMIT 1;"),
        ("Total Spent by First Name",
         "SELECT first_name, SUM(order_total) as 'Total Spent' FROM users JOIN orders ON users.id = orders.customer_id GROUP BY first_name ORDER BY SUM(order_total);"),
        ("Number of Orders by First Name",
         "SELECT first_name, COUNT(orders.id) as 'Number of Orders' FROM users JOIN orders ON users.id = orders.customer_id GROUP BY first_name ORDER BY COUNT(orders.id);"),
        ("Average Total per Order by First Name",
         '''
         SELECT users.first_name, ROUND(AVG(orders.order_total), 2) AS average_total_per_order
         FROM orders
         JOIN users ON orders.customer_id = users.id
         GROUP BY users.first_name
         ORDER BY average_total_per_order;
         ''')
    ]

    for i, (title, query) in enumerate(queries, start=0):
        filename = f'query_{str(i).zfill(2)}.png'
        execute_query_and_plot_df(query, 'Category', 'Value', title, filename, config)

if __name__ == "__main__":
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'KNOWLEDGE_MAPPING',
        'raise_on_warnings': True
    }
    main(config)
