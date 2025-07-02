#What is the most purchased item on the menu and how many times was it purchased by all customers?

select product_name, count(product_name) times
from sales
join menu
on sales.product_id = menu.product_id
group by product_name
order by times desc
limit 1;