# SAP BTP Data-to-Value Bootcamp
This SAP BTP Data-to-Value Bootcamp is developed and delivered by Partner Ecosystem Success Organization (formerly known as GPO) of SAP SE, which aims to accelerate SAP partner adoption of SAP BTP Data-to-Value. The bootcamp uses an end-to-end storyline about a bookshop, helping the bookshop manager to turn the data into business values with the SAP BTP solution portfolio about database, data management & analytics. 

<br/><br/>The bootcamp events are organized and delivered through SAP Learning Hub with a format of presentation, demo and exercise, which lasts 3~4 hours each day and 3 days in total. In addition, the system access of this bootcamp are prepared for the participants by SAP organizer. However, the system requirement and data preparation is also documented in this repository, where you can build up your own system landscape to complete this bootcamp on your own.
<br/>
At the end of the bootcamp, a badge will be issued by SAP to those participants who have gone throughout the whole bootcamp  and completed all the exercise tasks as a recognition of achievement.
<br/><br/>
The bookshop solution is a popular example of SAP Cloud Application Programing Model (CAP) for side-by-side extensibility with SAP BTP, also as an exercise of our SAP BTP Extension Suite Bootcamp. 

## Description
This GitHub repository contains the dataset, exercises, and sample code for the SAP BTP Data-to-Value Bootcamp. Covering an end-to-end data-to-value process with the database, data management & analytics solution portfolio of SAP Business Technology Platform such as: 
- SAP HANA Cloud Service (HCS) 
- SAP Data Warehouse Cloud (DWC)
- SAP Data Intelligence Cloud (DI)
- SAP Analytics Cloud (SAC)
<br/>

### Agenda
The agenda of this bootcamp is structured as process-oriented as below instead of product-oriented.
- Data Provisioning and Integration (HCS,DWC,DI)
- Data Modeling and Processing (DWC,DI)
- Data Virtualization and Analytics (SAC) 

### Storyline
![Bookshop Data-to-Value Storyline](resources/bookshop-d2v-storyline.png)

John, the owner of an online bookshop business named Amilka Bookshop Ltd. based in London, as a fan of Roald Dahl since childhood in the 80's who has a dream of owning a bookshop in his neighborhood with heaps of attractive children literature collections, has started his own bookshop business since 2011 as an online bookshop web shop specializing in children literature. Later in-house bookshop management implements a local ERP for finance and operation. As the business grows and expands geographically, in late 2020, John has hired an SAP partner to replace the local ERP with a modern modular cloud ERP -- SAP S/4HANA Cloud -- and migrate the legacy bookshop management solution to SAP HANA Cloud with SAP Cloud Application Programing Model with seamless integration with SAP S/4HANA Cloud. The historical book sales data from 2011 to 2020 are extracted from legacy ERP into csv files. The project has successfully gone live since beginning of 2021. Since then the book sales have been maintained in SAP S/4HANA Cloud, so is the book catalog and online orders are managed with the new bookshop solution powered by SAP HANA Cloud and SAP Cloud Application Programing Model.  <br/>

Given the business data accumulated for the past decade, John realizes that he could have making use of these data for:
- smart business insight and decision making 
- intelligent business planning
- operational efficiency improvement with automation
- reimagining the business with new services or products
- ...

The data landscape of Amilka Bookshop Ltd. as:
- bookshop solution (books, authors, genres, etc.) in SAP HANA Cloud
- active book sales data since 2021 from SAP S/4HANA Cloud
- archived historic book sales data from 2011 to 2020 in AWS S3

As an SAP partner, you’ll help John to address business questions such as:
- quarterly books sales trend
- top best-selling books/authors, and drill down to insight about specific book sales trend etc.
- book sales forecast and planning
- book recommendation with machine learning to improve the customer purchasing experience and upsales.
- book genre clustering with machine learning to automate the book genre prediction for new books. 
- ...

### Solution Architecture
![Bookshop Data-to-Value Solution Architecture](resources/bookshop-d2v-architecture.png)

### Final Outcomes of the Storyline
#### Bookshop Sales Overview
![Bookshop Sales Overview](resources/bookshop-sales-overview.png)

#### Book Sales Forecast
![Book Sales Overview](resources/book-sales-forecast.png)

## Requirements
### System Access Prerequisites
The system prerequisites below only apply to the self-pace learning without attending our BTP Data-to-Value bootcamp organized by the Partner Ecosystem Success organization of SAP, which all these system accesses are prepared and communicated by SAP to the participants who attend the bootcamp.
- An SAP HANA Cloud instance (trial version is fine) for bookshop solution
    - Provision a SAP HANA Database instance of SAP HANA Cloud Service used by the bookshop solution. Required by self-pace learning without attending the bootcamp, which has been prepared with Technical Academy Environment
    - Obtain the SAP HANA Database Explorer URL, HANA Database User and Password to the target SAP HANA Cloud Service through you SAP HANA Cloud central.
- An SAP S/4HANA Cloud tenant for book products and active sales orders of books since 2021
- An AWS S3 bucket for archived historic book sales orders from 2011 to 2020
- An SAP Data Warehouse Cloud tenant. (Trial version will have the limitation of HANA Machine Learning, which is used in one exercise about Book Recommendation.)
- An SAP Data Intelligence Cloud tenant (trial version is fine)
- An SAP Analytics Cloud tenant (trial version is fine)

### Knowledge Prerequisites
For the day 2 of the bootcamp, we have covered two machine learning scenarios, 
- one for book recommendation with SAP HANA Machine Learning 
- the other for book genre clustering with sklearn. 

Therefore, in order to have an effective learning, the participants should teach themselves with this openSAP course about [Get Started with Data Science (Edition 2021)](https://open.sap.com/courses/ds3)

## How to obtain support

[Create an issue](https://github.com/SAP-samples/<repository-name>/issues) in this repository if you find a bug or have questions about the content.

For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## License
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
