import os

from modules.base_config import db_session
from modules.constats import BASE_DIR
from modules.helper import (
    add_or_update_coord,
    update_time_subscription,
    update_time_time_send_sub,
    del_time_time_send_sub,
)

# print(os.path.join(BASE_DIR, "base.db"))

# add_or_update_coord(
#     2, "Dnipro", "UA", "48.450001",	"34.98333", None
#
# )
# update_time_time_send_sub(2, "08:15")
# add_or_update_coord(
#     3, "Dnipro", "UA", "48.450001",	"34.98333", None
#
# )
# update_time_time_send_sub(3, "08:15")
# add_or_update_coord(
#     4, "Dnipro", "UA", "48.450001",	"34.98333", None
#
# )
# update_time_time_send_sub(4, "08:15")
from modules.models import Users

# del_time_time_send_sub(353693694)

db_session.query(Users).filter(Users.id_user == 353693694).update(
    {"subscription": "2019-09-02 08:15:00"}
)
db_session.commit()
