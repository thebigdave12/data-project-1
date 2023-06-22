############################# TO DO #####################################
##### write import statements #####
import psycopg2
from psycopg2 import Error

from database import get_connected

try:
    # connection to database

    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()
  
############################# TO DO #####################################
    ############# SQL QUERIES TO EXTRACT INFORMATION #################

    #### create master_query variable
    master_query = """ SELECT * 
    FROM invoices
    JOIN customers on 
    invoices.customer_id = customers.id
    """
    #### create outdoors_query variable
    outdoors_query = """ SELECT *
    FROM invoices
    JOIN customers on 
    invoices.customer_id = customers.id
    WHERE product_category = 'Outdoors'
    """
    #### create garden_query variable
    garden_query = """SELECT *
    FROM invoices
    JOIN customers on 
    invoices.customer_id = customers.id
    WHERE product_category = 'Garden'
    """
    #### create product_revenue variable
    product_revenue = """SELECT product_category,
    SUM(unit_price*quantity) FROM invoices
    GROUP BY product_category
    ORDER BY SUM DESC
    """
############################# TO DO ####################################
    ############ COPYING SQL QUERY OUTPUTS TO CSV FILES #############

    #### create master_output variable with formatted master_query
    master_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(master_query)
    #### create outdoors_output variable with formatted outdoors_query
    outdoors_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(outdoors_query)
    #### create garden_output variable with formatted garden_query
    garden_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(garden_query)
    #### create product_revenue_output variable with formatted product_revenue_query
    product_revenue_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(product_revenue)
############################# TO DO ####################################
############## CREATING CSV FILES FROM OUTPUTS #########################

    #### create master.csv with open(...) function ####
    with open("master.csv", 'w') as file:
        cursor.copy_expert(master_output, file)
        print("Master.csv file has been created...")
    #### create outdoors.csv with open(...) function ####
    with open("outdoors.csv", 'w') as file:
        cursor.copy_expert(outdoors_output, file)
        print("Outdoors.csv file has been created...")
    #### create garden.csv with open(...) function ####
    with open("garden.csv", 'w') as file:
        cursor.copy_expert(garden_output, file)
        print("Garden.csv file has been created...")
    #### create product_revenue.csv with open(...) function ####
    with open("product_revenue.csv", 'w') as file:
        cursor.copy_expert(product_revenue_output, file)
        print("Product_revenue.csv file has been created...")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")