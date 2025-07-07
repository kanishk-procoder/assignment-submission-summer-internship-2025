select event_type, count(event_type)
from events
group by event_type;