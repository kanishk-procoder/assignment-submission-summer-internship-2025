#Which item was the most popular for each customer?

select * from 

(select sales.customer_id, menu.product_name, count(*) as ordered_times
from sales join menu
on sales.product_id = menu.product_id
group by customer_id, product_name) as x

where x.ordered_times in
(select max(y.ordered_times) as times_ordered
from 

(select sales.customer_id, menu.product_name,  count(*) as ordered_times
from sales join menu
on sales.product_id = menu.product_id
group by sales.customer_id, menu.product_name) as y 

where x.customer_id = y.customer_id
);
