from sqlalchemy import Column, String, Integer, TIMESTAMP, VARCHAR, ForeignKey

# from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

# from sqlalchemy_imageattach.entity import Image, image_attachment

from base_config import Base, engine


class Users(Base):
    __tablename__ = "users"

    id_row = Column(Integer, primary_key=True, autoincrement=True)
     id_user = Column(Integer, unique=True)
    city = Column(String)
    country_cod = Column(String)
    lat = Column(String)
    lon = Column(String)
    subscription = Column(TIMESTAMP)
    time_send_sub = Column(TIMESTAMP)
    timezone = Column(Integer)
    status = Column(Integer, default=0)
    data_sity_dict = Column(VARCHAR(200))
    time = Column(TIMESTAMP, default=now())

    def __init__(self, id_user, city, country_cod, lat, lon, timezone, status):
        self.id_user = id_user
        self.city = city
        self.country_cod = country_cod
        self.lat = lat
        self.lon = lon
        self.timezone = timezone
        self.status = status

    def chech_locate_null(self):
        if self.country_cod:
            return True
        else:
            return False

    def get_data_location(self):
        return {"city": self.city, "lat": self.lat, "lon": self.lon}


class Statistic(Base):
    __tablename__ = "statistic"

    id_row = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer)
    action = Column(String)
    time = Column(TIMESTAMP, default=now())

    def __init__(self, id_user, action):
        self.id_user = id_user
        self.action = action


class PR_modul(Base):
    __tablename__ = "pr_modul"

    id_row = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    url = Column(String)
    # picture = image_attachment('Pr_Picture')
    path_image = Column(String(100))

    def __init__(self, name, url):
        self.name = name
        self.url = url


# class Pr_Picture(Base, Image):
#     """User picture model."""
#
#     user_id = Column(Integer, ForeignKey('pr_modul.id_row'), primary_key=True)
#     user = relationship('PR_modul')
#
#     __tablename__ = 'pr_picture'


def init_db():
    # import model.admin # from model.admin import User doesnt help either
    # import model.role
    Base.metadata.create_all(bind=engine)
    # Base.metadata.drop_all(bind=engine)
    #
    # Base.metadata.reflect(bind=engine)


if __name__ == "__main__":
    init_db()
