using CatalogService from '../../srv/cat-service';

////////////////////////////////////////////////////////////////////////////
//
// Books Object Detail Page
//
annotate CatalogService.Books with @(UI : {
    HeaderInfo        : {
        TypeName       : '{i18n>Book}',
        TypeNamePlural : '{i18n>Books}',
        Description    : {Value : author}
    },
    HeaderFacets      : [{
        $Type  : 'UI.ReferenceFacet',
        Label  : '{i18n>Description}',
        Target : '@UI.FieldGroup#Descr'
    }, ],
    Facets            : [{
        $Type  : 'UI.ReferenceFacet',
        Label  : '{i18n>Details}',
        Target : '@UI.FieldGroup#Price'
    }, ],
    FieldGroup #Descr : {Data : [{Value : descr}, ]},
    FieldGroup #Genre : {Data : [{Value : genre.ID}, ]},
    FieldGroup #Price : {Data : [
        {Value : price},
        {
            Value : currency.symbol,
            Label : '{i18n>Currency}'
        },
    ]},
});

////////////////////////////////////////////////////////////////////////////
//
// Books Object Master List Page
//
annotate CatalogService.Books with @(UI : {
    SelectionFields : [
        ID,
        price,
        currency_code
    ],
    LineItem        : [
        {Value : title},
        {
            Value : author,
            Label : '{i18n>Author}'
        },
        {
            Value : genre.name,
            Label : '{i18n>Genre}'
        },
        {Value : price},
        {
            Value : currency.symbol,
            Label : ' '
        },
    ]
}, );
