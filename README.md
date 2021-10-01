# SAP BTP Data-to-Value Workshop

## Description
This repo contains a dataset, exercises, and sample code for a workshop scenario covering the end-to-end data-to-value with the database, data management & analytics solution portofilio of SAP Business Technology Plaform such as 
- SAP HANA Cloud Service(HCS) 
- SAP Data Warehouse Cloud(DWC)
- SAP Data Intelligence Cloud(DI)
- SAP Analytics Cloud(SAC)
<br/>  
The agenda of this workshop is structured as process-oritented as below instead of product-oritented.
- Data Provisioning and Integration(HCS,DWC,DI)
- Data Modeling and Processing(DWC,DI)
- Data Virtualization and Analytics(SAC) 

### Storyline
![Bookshop Data-to-Value Storyline](resources/bookshop-d2v-storyline.png)
John, the owner of an online bookshop business named Amilka Bookshop Ltd based in London, as a fan of Roald Dahl since childhood in 80s who has a dream of owning the bookshop in his nabourhood with heaps of attrative children literature collections, has started his own bookshop busines since 2011 as an online bookshop web shop specialising on children literature. Later in-house bookshop management solution and implemented a local ERP for finance and operation. As the business grows and geographical expansion, in late 2020, John has hired an SAP Partner to replace the local ERP with a modern modular cloud ERP-SAP S/4HANA Cloud, and migrate the legacy bookshop management solution to SAP HANA Cloud with SAP Cloud Application Programing Model with sealess integration with SAP S/4HANA Cloud. The historical book sales data from 2011 to 2020 are extrated from legacy ERP into csv files. The project has successfully gone live since beginning of 2021. Since then the book sales has been maintained in SAP S/4HANA Cloud, so is the book catalog and online orders are managed with the new bookshop solution powered by SAP HANA Cloud and SAP Cloud Application Programing Model.  <br/>

Given the business data accumulated for the past decade, John realises that he could have maken use of these data for 
- smarter business insight and decision making 
- more intelligent business planning
- operational efficiency improvement with automation 
- ...

The data landscape of Amilka Bookshop Ltd as:
- bookshop solution(books, authors, genres, etc.) in SAP HANA Cloud
- active book sales data since 2021 from SAP S/4HANA Cloud
- archived historic book sales data from 2011 to 2020 in AWS S3

As an SAP partner, you’ll help to address business questions such as:
- quarterly books sales trend
- top best-selling books/authors, and drill down to insight about specific book sales trend etc
- book sales forecast and planning
- book recommendation with machine learning to improve the customer purchasing experience and upsales.
- book genre clustering with machine learning to  
- ...

### Solution Architecture
![Bookshop Data-to-Value Solution Architecture](resources/bookshop-d2v-architecture.png)

## Requirements
### System Access Prerequisites
The system prerequisites below only apply to the self-pace learning without attending our BTP Data-to-Value workshop organised by the Partner Ecosystem Success organisation of SAP, which all these system accesses are prepared and communicated by SAP to the participants who attend to the workshop.
- An SAP HANA Cloud instance(trial version is fine) for bookshop solution
    - Provision a SAP HANA Database instance of SAP HANA Cloud Service used by the bookshop solution. Required by self-pace learning without attending the workshop, which has been prepared with Technical Academy Environment
    - Obtain the SAP HANA Database Explorer URL, HANA Database User and Password to the target SAP HANA Cloud Service through you SAP HANA Cloud central.
- An SAP S/4HANA Cloud tenant for book products and active sales orders of books since 2021
- An AWS S3 bucket for archived historic book sales orders from 2011 to 2020
- An SAP Data Warehouse Cloud tenant.(Trial version will have the limitation of HANA Machine Learning, which is used in one exercise about Book Recommendation.)
- An SAP Data Intelligence Cloud tenant.(Trial version is fine)
- An SAP Analytics Cloud tenant.(Trial version is fine)

### Knowledge Prerequisites
For the day 2 of the workshop, we have covered two machine learning scenarios, 
- one for book recommendation with SAP HANA Machine Learning 
- the other for book genre clustering with sklearn. 

Therefore, in order to have an effective learning, the participants should teach themselve with this openSAP course about [Get Started with Data Science (Edition 2021)](https://open.sap.com/courses/ds3)

## Download and Installation

## Known Issues

## How to obtain support

[Create an issue](https://github.com/SAP-samples/<repository-name>/issues) in this repository if you find a bug or have questions about the content.
 
For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## Contributing

## License
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
