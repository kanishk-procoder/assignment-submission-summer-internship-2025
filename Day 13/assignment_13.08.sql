select product_category, count(case when event_type = 1 then 1 end), count(case when event_type = 2 then 1 end)
from
events join page_hierarchy 
on events.page_id = page_hierarchy.page_id
join event_identifier
on events.event_type = event_identifier.event_type
where page_hierarchy.product_category is not null
group by page_hierarchy.product_category;