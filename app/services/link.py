import string
import random
from app.repositories.link import LinkRepository
from sqlalchemy.orm import Session


class LinkService:
    def __init__(self):
        self.linkRepo = LinkRepository()

    def generate_code(self, length: int = 6) -> str:
        alphabet = string.ascii_letters + string.digits
        return ''.join(random.choice(alphabet) for _ in range(length))

    def create_short_link(self, db: Session, url: str):
        candidate = self.linkRepo.get_by_url(db, url)

        if candidate:
            return candidate.short_code

        code = self.generate_code()

        # TODO: дописать проверку, что такого кода нет

        self.linkRepo.create(db, url, code)
        return code


    # TODO: написать метод, который будет возвращать оригинальый урл по коду