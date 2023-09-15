import mysql.connector #base cmd to import MySQL
db = mysql.connector.connect (
    host = "a-4368-project.chjrccumbafm.us-east-1.rds.amazonaws.com",
    user = "admin1",
    password = "apple123",
    database = "hwone",
)
# I need to create a cursor to interact with the database
cursor = db.cursor(dictionary=True)

# Let's find out all the unique sellers in the database
cursor.execute("SELECT DISTINCT seller FROM sales")
sellers = [row['seller'] for row in cursor.fetchall()]

# I will show the user all available sellers
print("Available Sellers:")
for seller in sellers:
    print(seller)

# Now I will ask the user to enter a seller's name
seller_name = input("Enter the seller's name: ")

# Let's get all sales data for the chosen seller
cursor.execute(f"SELECT * FROM sales WHERE seller = '{seller_name}'")
sales_data = cursor.fetchall()

# I am going to calculate the total sales for the seller
total_sales = 0.0  # I am using a float variable to store total sales

# I will show the user all sales details for the chosen seller
print(f"Sales Report for {seller_name}:")
for sale in sales_data:
    # Calculating the total sales value for each product
    total = float(sale['quantity']) * float(sale['price'])  # Converting quantity and price to float before multiplying
    total_sales += total

    # Showing the sales details to the user
    print(f"- Product: {sale['product']}, Quantity: {sale['quantity']}, Price: {sale['price']}, Total: {total:.2f}")

# Now I will show the total sales value to the user
print(f"Total Sales for {seller_name}: ${total_sales:.2f}")

# I shouldn't forget to close the database connection at the end
db.close()