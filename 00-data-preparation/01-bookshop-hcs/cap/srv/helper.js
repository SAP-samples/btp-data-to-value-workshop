const { BusinessPartner } = require("@sap/cloud-sdk-vdm-business-partner-service");
const _prepareBpBody = (bp) => {
    return {
        firstName: bp.FirstName,
        lastName: bp.LastName,
        businessPartnerCategory: bp.BusinessPartnerCategory
    }
}
const buildBusinessPartnerForCreate = (req) => {
    const bp = BusinessPartner.builder().fromJson(_prepareBpBody(req.data));
    return bp;
}
function formatBPResultsForCAPOData(businessPartners) {
    const jsonFormatForCAPOdataBP = [];
    businessPartners.forEach(businessPartner => {
        jsonFormatForCAPOdataBP.push(
            {
                BusinessPartner: businessPartner.businessPartner,
                FirstName: businessPartner.firstName,
                LastName: businessPartner.lastName,
                Industry: businessPartner.Industry,
                BusinessPartnerCategory: businessPartner.businessPartnerCategory
            });
    });
    return jsonFormatForCAPOdataBP;
}
module.exports = {
    buildBusinessPartnerForCreate,
    formatBPResultsForCAPOData
}