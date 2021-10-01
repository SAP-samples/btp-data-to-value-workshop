const cds = require('@sap/cds');
const { BusinessPartner } = require("@sap/cloud-sdk-vdm-business-partner-service");
const sdkDest = { "destinationName": 'S4HC' };
const {
    buildBusinessPartnerForCreate,
    formatBPResultsForCAPOData
} = require('./helper');
//here is the service implementation
//here are the service handlers
module.exports = cds.service.impl(async function () {
    const { Customers } = this.entities;
    const { Books, Orders } = cds.entities

    this.on('CREATE', Customers, async (req) => {
        try {
            const bp = buildBusinessPartnerForCreate(req);
            const result = await BusinessPartner
                .requestBuilder()
                .create(bp)
                .execute(sdkDest);
            return result;
        } catch (err) {
            req.reject(err);
        }
    });
    this.on('READ', Customers, async (req) => {
        /** [START] SCENARIO A
        * Connect with Cloud SDK to S4 to retrieve ALL customers
        * Return results as ALL customers.
        */
        // const s4bp = await BusinessPartner.requestBuilder()
        //     .getAll()
        //     .select(
        //         BusinessPartner.BUSINESS_PARTNER,
        //         BusinessPartner.FIRST_NAME,
        //         BusinessPartner.LAST_NAME,
        //         BusinessPartner.INDUSTRY,
        //         BusinessPartner.BUSINESS_PARTNER_CATEGORY)
        //     .execute(sdkDest);
        // return formatBPResultsForCAPOData(s4bp);
        /** [END] */
        /** [START] SCENARIO B
        * Connect with Cloud SDK to S4 to retrieve ALL customers
        * Match customers with existing orders in Bookshop
        * Return results ONLY Bookshop customers.
        */

        const bookshopOrders = await cds.read('Orders');
        const bookshopCustomers = [];
        const s4bp = await BusinessPartner.requestBuilder()
            .getAll()
            .select(
                BusinessPartner.BUSINESS_PARTNER,
                BusinessPartner.FIRST_NAME,
                BusinessPartner.LAST_NAME,
                BusinessPartner.INDUSTRY,
                BusinessPartner.BUSINESS_PARTNER_CATEGORY)
            .execute(sdkDest);
        var bp = formatBPResultsForCAPOData(s4bp);
        for (let i = 0; i < bp.length; i++) {
            var cust = bp[i].BusinessPartner
            for (let k = 0; k < bookshopOrders.length; k++) {
                if (cust == bookshopOrders[k].customer) {
                    // BP is Bookshop Customer
                    bookshopCustomers.push(bp[i]);
                }
            }
        }
        return bookshopCustomers;

        /** [END] */
    });
});
