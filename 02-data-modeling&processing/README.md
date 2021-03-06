# Data Modeling&Processing
In this section, we'll perform the following exercises
- End-to-end Modeling with SAP Data Warehouse Cloud for Book Sales Analysis
- End-to-end Machine Learning with SAP Data Intelligence Cloud for
    - Book Recommendation
    - Book Genre Clustering
## DV200-SAP Data Warehouse Cloud Modeling
![End-to-end Modeling with SAP Data Warehouse Cloud](../resources/dwc-modeling-exercise.png)
- [DV200_Exercise01](exercises/DV200_Exercise01_Data_Builder_Graphical_View_Creation_for_Book_Author_View.pdf): Create a Book Author view with Graphical View of Data Builder<br/>
[Demo Video](https://www.youtube.com/watch?v=-8iw7rxSogE&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=12)
- [DV200_Exercise02](exercises/DV200_Exercise02_Data_Builder_Data_Flow_Creation_for_Book_Sales_Order.pdf): Create a Data Flow to union the current sales orders in SAP S/4HANA Cloud and archived historic sales order in AWS S3, and persist the result as a local table.<br/>
[Demo Video](https://www.youtube.com/watch?v=VX4Kd82FfOY&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=13)
- [DV200_Exercise03](exercises/DV200_Exercise03_Business_Builder_Dimension_View_Creation_for_Book_Author_Dimension.pdf): Create a Dimension based on Book Author view<br/>
[Demo Video](https://www.youtube.com/watch?v=NQolwctu9hQ&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=14)
- [DV200_Exercise04](exercises/DV200_Exercise04_Business_Analytical_Dataset_Creation_for_Book_Sales_Order.pdf): Create a Analytical Dataset about All Book Sales Orders based on result of DV200_Exercise02 with association to Book Author Dimension and Day Dimension.<br/>
[Demo Video](https://www.youtube.com/watch?v=yXk0yp5He7w&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=15)
- [DV200_Exercise05](exercises/DV200_Exercise05_Business_ConsumptionModel_Perspective_Creation_for_Book_Sales_Order.pdf): Create a Comsumption Model based on the analytica dataset created in DV200_Exercise04, and create a perspective for the consumption model about All Book Sales Order with all fields.<br/>
[Demo Video](https://www.youtube.com/watch?v=KRsVEdK94ok&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=16)
- [DV200_Exercise06_Bonus_Exercise](exercises/DV200_Exercise06_Bonus_Exercise_Data_Builder_Graphical_View_Creation_for_V_BL_Sales_Dataset.pdf): This is a bonus exercise about modeling, which let you explore different options of modeling for the same use case. In this exercise, you will create another graphical view with data builder based on the book author view created in DV200_Exercise01, the time dimension-day view, and all_book_sales_order local table in DV200_Exercise02, which can produce the same output as DV200_Exercise05 for consumption.

## End-to-end Machine Learning with SAP Data Intelligence Cloud
![Machine Learning Exercises with SAP Data Intelligence Cloud](../resources/di-ml-exercise.png)
- [DV210_Exercise01](exercises/DV210_Exercise01_Book_Recommendation_with_SAP_HANA_Machine_Learning.pdf): Book Recommendation with SAP HANA Machine Learning. The related Jupyter Notebook is available [here](exercises/DV210_Exercise01_Book_Recommendation.ipynb) for referene. <br/>
  [Demo#1-Book Recommendation with SAP HANA Machine Learning via Jupiter Notebook](https://www.youtube.com/watch?v=iYrvlq9_9EM&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=19)<br/>
  [Demo#2-Custom operator about HANA ML training for book recommendation](https://www.youtube.com/watch?v=HfY6g6Wmz6Y&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=21)
- [DV220_Exercise01](exercises/DV220_Exercise01_Book_Genre_Clustering_via_Text_Classification_and_Clustering_with_Python.pdf): Book Genre Clustering via Text Classification and Clustering with Python. The related Jupytor Notebook is available [here](exercises/DV220_Exercise01_Book_Genre_Clustering.ipynb) for referene.
    - [Demo#1-Book Genre Clustering with Python](https://www.youtube.com/watch?v=AQ4zCWn7y-0&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=20)
    - [Demo#2-ML Training Pipeline with SAP Data Intelligence Cloud](https://www.youtube.com/watch?v=KNFaD-dopbk&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=22)
    - [Demo#3 ML Serving Pipeline with SAP Data Intelligence Cloud](https://www.youtube.com/watch?v=T9sWKaxOUQg&list=PLUvT3ZwlN9W3iXfnhh8CW2VKxSnf3bcCc&index=23)

## License
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](../LICENSES/Apache-2.0.txt) file.
