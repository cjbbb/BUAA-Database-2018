from Mysql import *
from Trigger import *
from app import app
from Commend import *

com = Commend()  # single instance model


def init():
    # create table
    Base.metadata.create_all(engine)

    # create trigger
    afterDeleteBuy()
    afterDeleteGame()
    afterDeleteUser()
    afterDeleteDeveloper()
    confirmBuy()


if __name__ == "__main__":
    init()
    app.run(debug='true')
