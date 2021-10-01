using {sap.capire.bookshop as my} from '../db/schema';

service CatalogService @(path : '/browse') {

    @readonly
    entity Books as
        select from my.Books {
            *, author.name as author, genre as genre
        }
        excluding {
            createdBy,
            modifiedBy
        };

    @requires_ : 'authenticated-user'
    action submitOrder(book : Books:ID, amount : Integer);
}