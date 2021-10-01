using {sap.capire.bookshop as my} from '../db/schema';

service AdminService @(path : '/manage') @(_requires : 'authenticated-user') {
    entity Books      as projection on my.Books;
    entity Authors    as projection on my.Authors;
    entity Orders     as projection on my.Orders;
    entity OrderItems as projection on my.OrderItems;

    entity Customers  as projection on my.Customers {
        BusinessPartner, LastName, FirstName, BusinessPartnerCategory
    };
}
