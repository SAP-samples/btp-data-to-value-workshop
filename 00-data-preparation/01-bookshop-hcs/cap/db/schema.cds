using {
    Currency,
    managed,
    sap,
    cuid
} from '@sap/cds/common';

namespace sap.capire.bookshop;

entity Books : managed {
    key ID           : Integer;
        title        : localized String(255);
        descr        : localized String(2000);
        author       : Association to Authors;
        genre        : Association to Genres;
        stock        : Integer;
        price        : Decimal(9, 2);
        currency     : Currency;
        isbn13       : String(13);
        avg_rating   : Decimal(9, 2);
        rating_count : Integer;
        publisher    : String(100);
}

entity Authors : managed {
    key ID           : Integer;
        name         : String(200);
        dateOfBirth  : Date;
        dateOfDeath  : Date;
        placeOfBirth : String;
        placeOfDeath : String;
        avg_rating   : Decimal(9, 2);
        books        : Association to many Books
                           on books.author = $self;
}

/**
 * Hierarchically organized Code List for Genres
 */
entity Genres : sap.common.CodeList {
    key ID       : Integer;
        parent   : Association to Genres;
        children : Composition of many Genres
                       on children.parent = $self;
}

entity Customers {
    key BusinessPartner         : String;
        LastName                : String;
        FirstName               : String;
        Industry                : String;
        BusinessPartnerCategory : String;
}

entity Orders : cuid, managed {
    OrderNo  : String       @title : 'Order Number'; //> readable key
    Items    : Composition of many OrderItems
                   on Items.parent = $self;
    customer : String;
    total    : Decimal(9, 2)@readonly;
    currency : Currency;
}

entity OrderItems : cuid {
    parent    : Association to Orders;
    book      : Association to Books;
    customer  : String;
    amount    : Integer;
    netAmount : Decimal(9, 2);
}
