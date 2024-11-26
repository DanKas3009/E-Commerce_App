# E-Commerce_App

The UML representation of the database

classDiagram
    class Customer{
        - fname
        - lname
        - email
        - password
        - ShippingAddress
        - phone
    }
    class Order {
        - orderID
        - OrderDate
        - CustomerID
        - OrderTotal
        - OrderStatus
        - ShippingAddress
    }

    class OrderDetails {
        - orderDetailsID
        - Order
        - Product
        - Quantity
        - Price
    }

    class Inventory {
        - inventoryID
        - Product
        - QuantityInStock
        - ReorderLevel
        - LastRestockDate
        - Location
    }

    class Product {
        - name
        - price
        - description
        - image
        - available
        - created
        - updated
    }

    class Cart {
        - cartID
        - customer
        - created_at
    }

    class CartItem{
        - ProductID
        - cartID
    }

    Customer "1" -- "1" Order
    Order "1" -- "*" OrderDetails
    OrderDetails "*" -- "1" Product
    Inventory "1" -- "*" Product
    Cart "1" -- "*" CartItem
    CartItem "*" -- "1" Product