from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.link import LinkRead, LinkCreate
from app.services.link import LinkService

router = APIRouter()
link_service = LinkService()


@router.post('/short', response_model=LinkRead)
def short(link_data: LinkCreate, db: Session = Depends(get_db)):
    code = link_service.create_short_link(db, url=str(link_data.url))
    return { "short_url": f'http://localhost:8000/{code}'}