# Welcome

This project is developed for the purpose of private partner bootcamp. Participants may clone the repository, install/build & run on your local environment or the SAP Business Application Studio. It is a use case to illustrate a simple bookshop management solution extended to S/4HANA Cloud with SAP Cloud SDK. _**To deploy this successful, please make sure you've the prior knowledge of [CAP](https://cap.cloud.sap/) and attended the bootcamp session.**_ 

## Use Case Scenario
![Use Case for this Project](https://github.com/jacobtan89/bootcamp-cap-bookshop/blob/master/Use%20Case.png?raw=true)

## Pre-requisites Check
Regardless if you're using Visual Studio code or SAP Business Application Studio, please ensure you have these components installed & setup in your local environment.

> Check the following (line-by-line) command if they have already been installed, if not, install them with the respective commands below.

```bash
node -v
cf --version
cds v
cf plugins
mbt --version
mta --version
```

> Install (line-by-line) on the respective libraries if any one of them above is missing.

```bash
npm install -g @sap/cds-dk
npm install -g @sap/cds
npm install -g mta
npm install -g mbt
cf install-plugin multiapps
```



## Let's Get Started
1. Clone into a bookshop folder.
```bash
git clone https://github.com/jacobtan89/bootcamp-cap-bookshop.git bookshop
```
2. Navigate into the _**bookshop**_ folder & install the _**required npm dependencies**_ declared in the package.json (takes about a few minutes).
```bash
cd bookshop
npm install
```
3. Run it with `cds watch` in your bookshop folder.
```bash
cds watch
```
4. `(Optional)` Connecting to your S/4 HANA Cloud System, please follow these steps.
* Create a destination in your SAP BTP account, pointing to your S/4 HANA Cloud system.
> Destination Name: `S4HC` 

> Destination URL: https://`<tenant>`.s4hana.ondemand.com

_Please note that the above destination name `S4HC` will be used in the Custom Logic file `Line 3` located in [srv/admin-service.js](srv/admin-service.js)._
In order to connect your app with the destination defined in your SAP BTP account, you can either create a local file `default-env.json` in your bookshop folder with the `destination` & `xsuaa` service key credentials **OR** simply just run everything in the cloud by packaging with MTA, build and deploy.

5. Package & Build with MTA then Deploy in your SAP BTP account.
- In your bookshop folder, package your app with the MTA Build Tool.
```bash
mbt build -t ./
```
- Once completed, let's deploy `bookshop_1.0.0.mtar` file in `bookshop` folder, to your SAP BTP Cloud Foundry environment..
```bash
cf deploy bookshop_1.0.0.mtar
```
If you face a problem with the example application or the description, feel free to create an [issue](https://github.com/jacobtan89/bootcamp-cap-bookshop/issues).

## Learn More

Learn more about the core concepts at [SAP Developer Tutorials on CAP Topic](https://developers.sap.com/tutorial-navigator.html?tag=software-product-function:sap-cloud-application-programming-model).

## License

Copyright (c) 2020 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed under SAP Sample Code License Agreement, except as noted otherwise in the [LICENSE](/LICENSE) file.