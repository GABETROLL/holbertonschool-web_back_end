-- Create a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
-- (the tables for the items on stock and orders
-- are in '4-init.sql',
-- and are named 'items' and 'orders')
CREATE TRIGGER IF NOT EXISTS decrease_item_quantity
    AFTER INSERT ON orders
    FOR EACH ROW UPDATE items SET  
;
