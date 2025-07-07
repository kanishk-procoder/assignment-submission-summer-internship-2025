select user_id, avg(count(cookie_id))
from users
group by user_id;