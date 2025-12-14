from typing import Union

from app.db.models import Link
from sqlalchemy.orm import Session


class LinkRepository:
    def get_by_url(self, db: Session, url: str) -> Union[Link, None]:
        return db.query(Link).filter_by(original_url=url).first()

    def get_by_code(self, db: Session, code: str) -> Union[Link, None]:
        return db.query(Link).filter_by(short_code=code).first()

    def create(self, db: Session, url: str, code: str) -> Link:
        link = Link(original_url=url, short_code=code)
        db.add(link)
        db.commit()
        db.refresh(link)
        return link