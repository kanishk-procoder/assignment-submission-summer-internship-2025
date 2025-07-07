select (count(visit_id)/(select count(distinct visit_id)
from events))*100 AS purchase_percnt
from events
where event_type = 3;