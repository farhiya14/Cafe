# Mini Project Week 5

CSV is great, but there is a better option. Let's store our couriers, and products in a database, we'll leave orders as they are for now.

An order's courier, and items properties currently use indexes to reference these entities, we're going to change this to use ids instead.

Remember to update unit-tests.

## Goals

As a user I want to:

- create a product, courier, or order and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier
- _BONUS_ track my product inventory
- _BONUS_ import/export my entities in CSV format

## Spec

- A `product` should be a `dict`, i.e:

```json
{
  "id": 4,
  "name": "Coke Zero",
  "price": 0.8
}
```

- A `courier` should be a `dict`, i.e:

```json
{
  "id": 2,
  "name": "Bob",
  "phone": "0789887889"
}
```

- An `order` should be a `dict`, i.e:

```json
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2, // Courier ID
  "status": "preparing",
  "items": [1, 3, 4] // Product IDs
}
```

- Data should be persisted to a `.csv` file on a new line for each `order`, ie:

```csv
# ORDER
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

## Pseudo Code

- START APP
- LOAD `ORDERS` FROM `CSV` FILE
- SELECT ALL FROM `PRODUCTS` AND `COURIERS` TABLE AND CACHE
- SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
- IF USER ENTERS `0` THEN SAVE `ORDERS` TO `CSV` FILE AND EXIT APP
- IF USER ENTERS `1` THEN SHOW `PRODUCT` MENU
  - IF USER ENTERS `0` RETURN TO MAIN MENU
  - IF USER ENTERS `1`
    - SELECT ALL FROM PRODUCTS TABLE AND CACHE
    - PRINT OUT PRODUCTS TO SCREEN
  - IF USER ENTER `2` CREATE NEW `PRODUCT`
    - ASK USER FOR THE `NAME` OF THE `PRODUCT`
    - ASK USER FOR THE `PRICE` OF THE `PRODUCT`
    - INSERT INTO `PRODUCTS` TABLE
    - UPDATE CACHED `PRODUCTS`
  - _STRETCH_ IF USER ENTERS `3` UPDATE `PRODUCT`
    - ASK USER TO SELECT A `PRODUCT` TO UPDATE OR `0` TO CANCEL
    - FOR EACH `PRODUCT` PROPERTY
      - ASK USER FOR UPDATED DATA OR LEAVE BLANK TO SKIP
      - UPDATE COLUMN IN DB IF NOT BLANK
      - UPDATE CACHED `PRODUCTS`
  - _STRETCH_ IF USER ENTERS `4` DELETE `PRODUCT`
    - ASK USER TO SELECT A `PRODUCT` TO DELETE OR `0` TO CANCEL
    - DELETE ROW FROM `PRODUCTS` TABLE
    - UPDATE CACHED `PRODUCTS`
- IF USER ENTERS `2` THEN SHOW `COURIER` MENU
  - IF USER ENTERS `0` RETURN TO MAIN MENU
  - IF USER ENTERS `1` PRINT OUT `COURIERS` TO SCREEN
  - IF USER ENTER `2` CREATE NEW `COURIER`
    - ASK USER FOR THE `NAME` OF THE `COURIER`
    - ASK USER FOR THE `PHONE` OF THE `COURIER`
    - INSERT INTO THE `COURIERS` TABLE
    - UPDATE CACHED `COURIERS`
  - _STRETCH_ IF USER ENTERS `3` UPDATE `COURIER`
    - ASK USER TO SELECT A `COURIER` TO UPDATE OR `0` TO CANCEL
    - FOR EACH `COURIER` PROPERTY
      - ASK USER FOR UPDATED DATA OR LEAVE BLANK TO SKIP
    - UPDATE COLUMNS IN `COURIERS` TABLE IF NOT BLANK
    - UPDATE CACHED `COURIERS`
  - _STRETCH_ IF USER ENTERS `4` DELETE `COURIER`
    - ASK USER TO SELECT A `COURIER` TO DELETE OR `0` TO CANCEL
    - REMOVE THIS ITEM FROM THE `COURIERS` TABLE
    - UPDATE CACHED `COURIERS`
- IF USER ENTERS `3` THEN SHOW `ORDER` MENU
  - IF USER ENTERS `0` RETURN TO MAIN MENU
  - IF USER ENTERS `1` PRINT OUT `ORDERS` TO SCREEN
  - IF USER ENTER `2` CREATE NEW `ORDER`
    - ASK USER FOR THE `NAME` OF THE `CUSTOMER`
    - ASK USER FOR THE `ADDRESS` OF THE `CUSTOMER`
    - ASK USER FOR THE `PHONE` OF THE `CUSTOMER`
    - ASK USER TO SELECT FROM THE `PRODUCT` LIST UNTIL `0` TO CANCEL
    - SET `ORDER PRODUCTS` TO BE A LIST OF `PRODUCT` IDS
    - ASK THE USER TO SELECT A `COURIER` FROM THE LIST
    - SET `ORDER COURIER` TO BE A `COURIER` ID
    - SET THE DEFAULT `ORDER STATUS` TO BE `PREPARING`
    - APPEND THE NEW ORDER TO THE LIST OF `ORDERS`
  - IF USER ENTERS `3` UPDATE `ORDER STATUS`
    - ASK USER TO SELECT AN `ORDER` TO UPDATE OR `0` TO CANCEL
    - ASK USER TO SELECT A NEW `STATUS` FROM A LIST OF STATUSES
    - UPDATE THE `ORDER`
  - _STRETCH_ IF USER ENTERS `4` UPDATE `ORDER`
    - ASK USER TO SELECT AN `ORDER` TO UPDATE OR `0` TO CANCEL
    - FOR EACH `ORDER` PROPERTY
      - ASK USER FOR UPDATED DATA OR LEAVE BLANK TO SKIP
      - UPDATE THE `ORDER` PROPERTY IF NOT BLANK
  - _STRETCH_ IF USER ENTERS `5` DELETE `ORDER`
    - ASK USER TO SELECT AN `ORDER` TO DELETE OR `0` TO CANCEL
    - REMOVE THIS ITEM FROM THE `ORDERS` LIST
