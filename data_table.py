from app import db
from models import Task
from datetime import datetime

if __name__ == "__main__":
    # fix problem by importing db from models.py instead: from models import db
    db.create_all()
    t1 = Task(title="xyz", date=datetime.utcnow())
    t2 = Task(title="abc", date=datetime.utcnow())
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()
    tasks = Task.query.all()