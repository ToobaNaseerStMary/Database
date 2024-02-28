from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from week5.database.database import DATABASE_PATH
from week5.persistence.entities.role import Role
class RoleCRUD:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        self.Session = sessionmaker(bind=self.engine)

    # create (could have multiple functions)
    def create_role(self, role_name):
        session = self.Session()
        try:
            role = {"RoleName": role_name}
            new_role = Role(**role)
            session.add(new_role)
            session.commit()
            return new_role
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    def retrieve(self, id):
        session = self.Session()
        try:
            return session.query(Role).filter_by(RoleID=id).first()
        finally:
            session.close()

    def retrieve_all_roles(self):
        session = self.Session()
        try:
            return session.query(Role).all()
        finally:
            session.close()

    def update_role(self, id, role_name):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()
            if role:
                role.RoleName = role_name
                session.commit()
            return role
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    def delete_role(self, id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()
            if role:
                session.delete(role)
                session.commit()
            return role
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()


