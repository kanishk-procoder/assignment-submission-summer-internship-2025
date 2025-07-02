#How many days has each customer visited the restaurant?

select customer_id, count(distinct order_date)
from sales
group by customer_id;