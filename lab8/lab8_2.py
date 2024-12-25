from datetime import datetime, timezone, time, date
from typing import Optional, List
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sender_id: Mapped[int] = mapped_column(sa.ForeignKey("sender.id"))
    reciever_id: Mapped[int] = mapped_column(sa.ForeignKey("reciever.id"))
    order_date: Mapped[date] = mapped_column(sa.Date, default=lambda: datetime.now(timezone.utc))
    delivery_date: Mapped[date] = mapped_column(sa.Date, nullable=False)
    price: Mapped[int] = mapped_column()
    courier_id: Mapped[int] = mapped_column(sa.ForeignKey('courier.id'), nullable=False)
    transport_id: Mapped[int] = mapped_column(sa.ForeignKey('transport.id'), nullable=False)

    transport: Mapped['Transport'] = relationship('Transport', back_populates='orders')
    reciever: Mapped['Reciever'] = relationship('Reciever', back_populates='orders')
    sender: Mapped['Sender'] = relationship('Sender', back_populates='orders')
    courier: Mapped['Courier'] = relationship('Courier', back_populates='orders')


class Transport(Base):
    __tablename__ = 'transport'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    model: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    registration_date: Mapped[date] = mapped_column(sa.Date, nullable=False)
    color: Mapped[str] = mapped_column(sa.String(20))

    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='transport')

class Reciever(Base):
    __tablename__ = 'reciever'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    first_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    patronymic_name: Mapped[Optional[str]] = mapped_column(sa.String(256))
    date_of_birth: Mapped[date] = mapped_column(sa.Date, nullable=False)
    index: Mapped[int] = mapped_column()
    city: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    street: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    house: Mapped[str] = mapped_column(sa.String(8), nullable=False)
    apartment: Mapped[Optional[str]] = mapped_column(sa.String(8))
    phone_number: Mapped[str] = mapped_column(sa.String(16), nullable=False)

    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='reciever')


class Sender(Base):
    __tablename__ = 'sender'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    first_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    patronymic_name: Mapped[Optional[str]] = mapped_column(sa.String(256))
    date_of_birth: Mapped[date] = mapped_column(sa.Date, nullable=False)
    index: Mapped[int] = mapped_column()
    city: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    street: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    house: Mapped[str] = mapped_column(sa.String(8), nullable=False)
    apartment: Mapped[Optional[str]] = mapped_column(sa.String(8))
    phone_number: Mapped[str] = mapped_column(sa.String(16), nullable=False)

    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='sender')


class Courier(Base):
    __tablename__ = 'courier'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    first_name: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    patronymic_name: Mapped[Optional[str]] = mapped_column(sa.String(256))
    passport_number: Mapped[str] = mapped_column(sa.String(32), nullable=False, unique=True)
    date_of_birth: Mapped[date] = mapped_column(sa.Date, nullable=False)
    hiring_date: Mapped[date] = mapped_column(sa.Date, nullable=False)
    start_of_working_day: Mapped[time] = mapped_column(sa.Time, nullable=False)
    end_of_working_day: Mapped[time] = mapped_column(sa.Time, nullable=False)
    city: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    street: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    house: Mapped[str] = mapped_column(sa.String(8), nullable=False)
    apartment: Mapped[Optional[str]] = mapped_column(sa.String(8))
    phone_number: Mapped[str] = mapped_column(sa.String(16), nullable=False, unique=True)

    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='courier')


if __name__ == "__main__":
    engine = sa.create_engine('sqlite:///lab8/orders.db', echo=True)
    Base.metadata.create_all(engine)    

    from sqlalchemy.orm import Session

    with Session(engine) as db_session:
        # Добавление записей в таблицу Courier
        couriers = [
            Courier(
                last_name="Petrov",
                first_name="Petr",
                patronymic_name="Petrovich",
                passport_number="8888 234567",
                date_of_birth=datetime(1990, 3, 15),
                hiring_date=datetime(2021, 2, 1),
                start_of_working_day=time(9, 0, 0),
                end_of_working_day=time(18, 0, 0),
                city="Saint Petersburg",
                street="Nevsky Prospekt",
                house="25",
                apartment="5",
                phone_number="+79991112233"
            ),
            Courier(
                last_name="Sidorov",
                first_name="Sidr",
                patronymic_name="Sidorovich",
                passport_number="9999 345678",
                date_of_birth=datetime(1988, 7, 10),
                hiring_date=datetime(2019, 6, 15),
                start_of_working_day=time(10, 0, 0),
                end_of_working_day=time(19, 0, 0),
                city="Kazan",
                street="Baumana",
                house="15",
                apartment="8",
                phone_number="+79993334455"
            )
        ]
        db_session.add_all(couriers)

        # Добавление записей в таблицу Sender
        senders = [
            Sender(
                last_name="Ivanov",
                first_name="Ivan",
                patronymic_name="Ivanovich",
                date_of_birth=datetime(1985, 5, 10),
                index=123456,
                city="Moscow",
                street="Tverskaya",
                house="10",
                apartment="23",
                phone_number="+79990001122"
            ),
            Sender(
                last_name="Smirnov",
                first_name="Sergey",
                patronymic_name="Sergeevich",
                date_of_birth=datetime(1992, 12, 20),
                index=654321,
                city="Minsk",
                street="Lenina",
                house="7",
                apartment="15",
                phone_number="+375291112233"
            )
        ]
        db_session.add_all(senders)

        # Добавление записей в таблицу Reciever
        recievers = [
            Reciever(
                last_name="Volkov",
                first_name="Vasiliy",
                patronymic_name="Vasilievich",
                date_of_birth=datetime(1987, 8, 25),
                index=111111,
                city="Kiev",
                street="Shevchenko",
                house="5",
                apartment="9",
                phone_number="+380501112233"
            ),
            Reciever(
                last_name="Kuznetsov",
                first_name="Dmitriy",
                patronymic_name="Dmitrievich",
                date_of_birth=datetime(1995, 3, 30),
                index=222222,
                city="Riga",
                street="Brivibas",
                house="20",
                apartment="12",
                phone_number="+37167112233"
            )
        ]
        db_session.add_all(recievers)

        # Добавление записей в таблицу Transport
        transports = [
            Transport(
                model="Ford Transit",
                registration_date=date(2019, 5, 15),
                color="White"
            ),
            Transport(
                model="Mercedes Sprinter",
                registration_date=date(2020, 8, 20),
                color="Black"
            )
        ]
        db_session.add_all(transports)

        # Добавление записей в таблицу Orders
        orders = [
            Orders(
                sender_id=1,
                reciever_id=1,
                order_date=date(2024, 12, 26),
                delivery_date=date(2024, 12, 30),
                price=5000,
                courier_id=1,
                transport_id=1
            ),
            Orders(
                sender_id=2,
                reciever_id=2,
                order_date=date(2024, 12, 27),
                delivery_date=date(2024, 12, 31),
                price=7000,
                courier_id=2,
                transport_id=2
            )
        ]
        db_session.add_all(orders)

        db_session.commit()