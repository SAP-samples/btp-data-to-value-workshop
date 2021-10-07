# Data Preparation for bookshop solution via SQL
In this section, we will prepare the data for the bookshop solution via SQL
- Creating the bookshop tables via SQL
- Import the data to the bookshop tables.

## Pre-requisites
- Obtain the SAP HANA Database Explorer URL, Database User and Password to the target SAP HANA Cloud Service.
- A database schema in place for bookshop solution. For participant attending the bootcamp, please use the schema assigned to you. 

## Steps to prepare the data for bookshop solution via SQL
### 1.Creating the bookshop tables via SQL
- Open a SQL Console from SAP HANA Database Explorer URL
- Copy the raw content of [bookshop_tables_initialisation.sql](bookshop_tables_initialisation.sql) and run on the SQL Console to create the bookshop tables.<br/>
As a result, the following tables have been created.
- SAP_CAPIRE_BOOKSHOP_BOOKS: Books Master Data
- SAP_CAPIRE_BOOKSHOP_GENRES: Book Genre ID and Name
- SAP_CAPIRE_BOOKSHOP_AUTHORS: Authors Master Data
- SAP_CAPIRE_BOOKSHOP_ORDERITEMS: Book Sales Order Items

### 2.Import the data into the bookshop tables
Please import the following tables with csv files in sequence through Catalog > Tables > Import Data in SAP HANA Database Explorer. Assure to select existing table created in step 1 instad of create new tables. Refer to [help portal](https://help.sap.com/viewer/a2cea64fa3ac4f90a52405d07600047b/cloud/en-US/ee0e1389fde345fa8ccf937f19c99c30.html) for more details about Import Data to SAP HANA Database, SAP HANA Cloud with SAP HANA Data Explorer 
- Table: CSV File
- SAP_CAPIRE_BOOKSHOP_GENRES: [genres.csv](../../00-dataset/genres.csv)
- SAP_CAPIRE_BOOKSHOP_AUTHORS: [authors.csv](../../00-dataset/authors.csv)
- SAP_CAPIRE_BOOKSHOP_BOOKS: [books.csv](../../00-dataset/books.csv)
- SAP_CAPIRE_BOOKSHOP_ORDERITEMS: [sales_order_items_all_extended.csv](../../00-dataset/sales_order_items_all_exended.csv)