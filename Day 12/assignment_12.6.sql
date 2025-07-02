#Which item was purchased first by the customer after they became a member?

select x.customer_id, m.product_name, x.first_o_date

from 

(select s.customer_id, min(s.order_date) as first_o_date
 from sales s 
 join members mem 
 on s.customer_id = mem.customer_id
 where s.order_date >= mem.join_date
 group by s.customer_id) as x

join sales s 
on x.customer_id = s.customer_id and x.first_o_date = s.order_date

join menu m 
on s.product_id = m.product_id

order by x.customer_id;
