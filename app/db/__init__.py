from sqlmodel import create_engine, Session, SQLModel, Field


class Config:
    # CLASS PROPERTIES
    ENGINE = create_engine("sqlite:///my_db.db")  # , echo=True)
    SESSION = Session(bind=ENGINE)

    @classmethod
    def migrate(cls):
        items = [Post(title=f"post#{x}", content=f"content{x}") for x in range(10)]
        cls.SESSION.add_all(items)
        cls.SESSION.commit()

    @classmethod
    def restart_db(cls):
        SQLModel.metadata.drop_all(bind=cls.ENGINE)
        SQLModel.metadata.create_all(bind=cls.ENGINE)
        # cls.migrate()


class IDAutoIncrement(SQLModel, table=False):
    id: int | None = Field(default=None, primary_key=True)


from .post import Post
