#What are the total items and amount spent for each member before they became a member?

select x.customer_id, sum(x.item_count) as total_items, sum(m.price * x.item_count) total_spend

from 

(select s.customer_id, s.product_id, count(1) as item_count
 from sales s 
 join members mem 
 on s.customer_id = mem.customer_id
 where s.order_date < mem.join_date
 group by s.customer_id, s.product_id) as x
 
join menu m 
on x.product_id = m.product_id

group by x.customer_id
order by x.customer_id;
