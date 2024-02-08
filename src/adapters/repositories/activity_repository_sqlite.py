"""
activity_repository_sqlite.py

Author: Otavio Abreu dos Santos Silva
Date: February 05, 2024
"""

from datetime import datetime
import sqlite3
from .activity_repository import ActivityRepository

class ActivityRepositorySqlite(ActivityRepository):
    """Activity Repository Implementatin for SQLite"""
    def __init__(self):
        self.conn = sqlite3.connect('mock.db')

    def insert_activity(self, name: str, description: str, status_code: int, creation_date: datetime):
        cursor = self.conn.cursor()

        query = f"""
            INSERT INTO todo(name, description, status, creation_date)
            VALUES(
                {name},
                {description},
                {status_code},
                {creation_date}
            );
        """

        try:
            cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def fetch_from_id(self, activity_id: int) -> tuple:
        cursor = self.conn.cursor()

        query = f"""
            SELECT * FROM todo WHERE id = {activity_id};
        """

        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

        return ()

    def fetch_from_name(self, name: str) -> tuple:
        cursor = self.conn.cursor()

        query = f"""
            SELECT * FROM todo WHERE name LIKE '{name}%';
        """

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

        return ()

    def fetch_from_status(self, status_code: int) -> tuple:
        cursor = self.conn.cursor()

        query = f"""
            SELECT * FROM todo WHERE status = {status_code};
        """

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

        return ()

    def fetch_from_date(self, starting_date: datetime, final_date: datetime) -> tuple:
        cursor = self.conn.cursor()
        parsed_starting = starting_date.strftime("%Y-%m-%d")
        parsed_final = final_date.strftime("%Y-%m-%d")

        query = f"""
            SELECT * FROM todo WHERE creation_date > {parsed_starting} and creation_date < {parsed_final};
        """

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

        return ()

    def update_activity(self, activity_id: int, name: str, description: str, status: int):
        cursor = self.conn.cursor()

        query = f"""
            UPDATE 
                todo 
            SET 
                name = {name},
                description = {description},
                status = {status}
            WHERE
                id = {activity_id};
        """

        try:
            cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def delete_activity(self, activity_id: int):
        cursor = self.conn.cursor()

        query = f"""
            DELETE FROM todo WHERE id = {activity_id};
        """

        try:
            cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
