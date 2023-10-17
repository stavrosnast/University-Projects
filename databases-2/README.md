# Databases 2 Project

## Hotel Room Reservation System

### Overview

This project aims to create a hotel room reservation system with the following key features:

1. **Home Page**: The Home page provides essential information about the hotel, including its category, offered services, the number of rooms, and more. It features photos of the hotel and the surrounding area, along with the hotel's address and contact details.

2. **Rooms Page**: The Rooms page offers descriptions and images of various room types, such as single, double, triple, and quadruple rooms.

3. **Reservation Page**: On the Reservation page, users can make bookings for one or more rooms during specific date ranges. To complete a reservation, users are required to fill out a contact information form.

4. **Contact Page**: The Contact page allows users to send messages or inquiries to the hotel.

#### Development Platform

This system will be developed using the XAMPP platform.

## Database Design

### Tables

1. **InsuranceCovers (Product) Table**
   - Attributes:
     - `prodcode` (Primary Key): Unique identifier for each insurance product.
     - `pname`: Name of the insurance product.
     - `anncost`: Annual cost of the insurance product.
     - `mintime`: Minimum term of validity for the insurance product.
     - `benefits`: Description of the benefits of the insurance product.

2. **Customer Table**
   - Attributes:
     - `custcode` (Primary Key): Unique identifier for each customer.
     - `cname`: Customer's name.
     - `csurname`: Customer's surname.
     - `address`: Customer's address.
     - `city`: Customer's city.
     - `tk`: Customer's postal code.
     - `phone`: Customer's telephone number.
     - `afm`: Customer's VAT number.
     - `poy`: Customer's POY (Place of Origin Year).

3. **Contract Table**
   - Attributes:
     - `contractcode` (Primary Key): Unique identifier for each contract.
     - `custcode` (Foreign Key): References the customer who signed the contract.
     - `prodcode` (Foreign Key): References the insurance product included in the contract.
     - `start_date`: Start date of the policy.
     - `end_date`: End date of the policy.
     - `cost`: Cost of the policy.

### Constraints

- Primary keys and foreign keys have been defined to ensure data integrity.
- Appropriate check constraints have been implemented to maintain data quality.
- Relationships between tables are established through foreign key constraints.

## SQL Queries

The following SQL queries can be executed in the database to retrieve policy statistics and customer costs:

### Query 1: Number of Policies by Insurance Product

This query provides the number of policies for each insurance product.

```sql
SELECT
    prod.pname AS InsuranceProduct,
    COUNT(contract.contractcode) AS NumberOfPolicies
FROM Product prod
LEFT JOIN Contract contract ON prod.prodcode = contract.prodcode
GROUP BY prod.pname;
```

### Query 2: Customers Sorted by Total Policy Cost (High to Low)

This query lists customers sorted by the total cost of their policies in descending order.

```sql
SELECT
    cust.cname AS CustomerName,
    SUM(contract.cost) AS TotalPolicyCost
FROM Customer cust
LEFT JOIN Contract contract ON cust.custcode = contract.custcode
GROUP BY cust.cname
ORDER BY TotalPolicyCost DESC;
```

## PHP Scripts

The PHP scripts included in this repository are part of a web application for managing the General Insurance Database. The main scripts are as follows:

1. **contacts.php**: This script allows users to select insurance products and displays customer information who have purchased the selected products.

2. **insert_am.php**: This script is used to search for contract details based on the date and VAT number (AFM) of the customer. It calculates the total number of active contracts and the total cost of the contracts for a specific customer and date.

3. **search.php**: This script processes the search parameters from `insert_am.php` and retrieves contract details and cost calculations.

4. **view.php**: This script displays all the insurance products (packages) stored in the database, including their attributes.

5. **index.html**: The main menu for the web application with options to view products, view contracts, and perform searches.
