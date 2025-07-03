#In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi — how many points do customer A and B have at the end of January?

select s.customer_id,
sum(
case 
when s.order_date between mem.join_date and date(mem.join_date+6)
then m.price*20

when m.product_name = "sushi"
then m.price*20

else m.price*10

end) as total_points

from sales s join members mem
on s.customer_id = mem.customer_id

join menu m
on s.product_id = m.product_id

where s.order_date < "2021-02-01"

group by s.customer_id;