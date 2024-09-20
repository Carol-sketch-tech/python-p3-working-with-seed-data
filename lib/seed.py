#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from models import Game,create_tables
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()


if __name__ == '__main__':
    
   
    # creating database engine
    engine = create_engine('sqlite:///seed_db.db')

    # creating tables
    create_tables(engine)

    # create a session.
    Session = sessionmaker(bind=engine)
    session = Session()

    # add a console message to indicate seeding.
    print('seeding games...')

    # this is to refresh the database to avoid duplication.
    session.query(Game).delete()
    session.commit()

    #creating a list of 50 random games
    games = [
        Game(
            title = fake.name(),
            genre = fake.word(),
            platform = fake.word(),
            price= random.randint(0, 60)
        )
        for _ in range(50)
    ]

    #statement to save these cahnges to the database.
    session.bulk_save_object(games)

    #statement to commit the session.
    session.commit()

    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    ccs = Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0)


    session.add_all([botw, ffvii, mk8, ccs])
    session.commit()