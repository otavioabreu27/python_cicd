import datetime

class ActivityRepository:
    def insert_activity(self, name: str, description: str, status_code: int, creation_date: datetime):
        pass

    def fetch_from_id(self, activity_id: int) -> tuple:
        pass

    def fetch_from_name(self, name: str) -> tuple:
        pass

    def fetch_from_status(self, status_code: int) -> tuple:
        pass

    def fetch_from_date(self, starting_date: datetime, final_date: datetime) -> tuple:
        pass

    def update_activity(
        self, activity_id: int, name: str, description: str, status: int
    ):
        pass

    def delete_activity(self, activity_id: int):
        pass