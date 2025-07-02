#If each $1 spent equates to 10 points and sushi has a 2x points multiplier — how many points would each customer have?

select s.customer_id, sum(if(m.product_name = "sushi", 20 * m.price, m.price * 10)) as total_points
from sales as s join menu as m 
on s.product_id = m.product_id
group by customer_id;