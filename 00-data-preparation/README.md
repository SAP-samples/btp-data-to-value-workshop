# Data Preparation for SAP BTP Data-to-Value Bootcamp
This bookshop dataset is designed for the SAP BTP Data-to-Value Bootcamp, which is based on the [British Library](https://www.bl.uk/collection-metadata/downloads) Dataset about Children's Literature under the [Creative Commons CC0 1.0 Universal Public Domain Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).

## Description about the dataset
This [bookshop dataset](00-dataset)(csv format) is made of
- [Books](00-dataset/books.csv) (10058 Children Books)
    - Book ID, Title, Description, Author ID, ISBN13 and Publisher are extract from British Library dataset with grounded truth. To simplify the data model, only the first author is extracted  in case of multiple authors for one book.
    - Genre ID: Default value as 0 - unknown, which will be clustered based on the title and description with machine learning algorithm as bootcamp exercise.  
    - Price: Randomly generated decimal value with two decimal place between 10.00~100.00
- [Authors](00-dataset/authors.csv): 2942 Authors associated with the books.Schema as Author ID, Name
- [Genres](00-dataset/genres.csv): 11 generes. Genre ID and Name(values as unknown,gener1~10 as placeholders), which will be updated after all books have been clustered based on the title and description with machine learning algorithm as bootcamp exercise.  
- Book Sales Order Items: 287,906 transaction records for the book sales since 2011. To simplify the data model, we only take sales order transaction for the Quote-to-Cash process. Delivery notes, Billing Document and Payments etc are not part of the dataset. <br>
The schema of sales order item except [Live Book Sales Order Items since 2021](00-dataset/sales_order_items_wide_s4hc.csv): order_ID, order_date, book_ID, quantity, net_amount
  - [Live Book Sales Order Items since 2021](00-dataset/sales_order_items_wide_s4hc.csv): The format as one or multiple book id, and order date. To be imported into your SAP S/4HANA Cloud tenant via [csv2s4 tool](https://github.com/Ralphive/csv2s4) by [@Ralphive](https://github.com/Ralphive). However, a ready-use SAP S/4HANA Cloud with this data will be prepared for you during our bootcamp.
  - [Archived Historic Book Sales Order Item for 2011~2020](00-dataset/sales_order_items_archived.csv): Stored in external cloud storage or data lake. In our bootcamp storyline, we take AWS S3 for example.

## Data Preparation
To simplify the data preparation for the bootcamp, we have prepared the data(Book Products, Book Sales Order since 2021) for SAP S/4HANA Cloud and archived historic sales order item for 2011~2020 in AWS S3 bucket. However, if you would like to go through this data-to-value journey on your own, you also can prepare the data in your own SAP S/4 HANA Cloud tenant and AWS S3.

### #1-Bookshop Solution Data in SAP HANA Cloud
The online bookshop solution data is stored in SAP HANA Database of SAP HANA Cloud, including the Books, Authors, Genres and Book Sales Order Items. The bookshop solution enables the booshop manager to maintain the book catalog, and the end customer of bookshop to place book order online, and synchronised to SAP S/4HANA Cloud for order-to-cash process.
<br/><br/>

#### Data Preparation Options for bookshop solution on SAP HANA Cloud.
- [data preparation via sql](01-bookshop-hcs/sql): Creating table structures and import the data via SQL. This approach will be used in our bootcamp for simplicity. Please follow this document step by step to prepare the bookshop data via sql.
- [data preparation via cap(SAP Cloud Application Programing Model) project deployment](01-bookshop-hcs/cap): This bookshop solution is forged from the [bookshop exercise project](https://github.com/jacobahtan/bootcamp-cap-bookshop)(part of our BTP Extension Suite bootcamp) prepared by our colleague [Jacob Tan](https://github.com/jacobahtan). We have updated it with our the bookshop dataset for data-to-value bootcamp. Have to acknowledge that it is orginally forged from the famous [cap sample about bookshop](https://github.com/SAP-samples/cloud-cap-samples/tree/master/bookshop) by a bunch of SAP CAP gurus from the community. To deploy the bookshop solution with data, please follow this document.

### #2-Book Products and Sales Order since 2021 in SAP S/4HANA Cloud

### #3-Archived Historic Book Sales Order items(2011~2020) in AWS S3


