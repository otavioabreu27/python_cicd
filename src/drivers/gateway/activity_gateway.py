"""
activity.py

Author: Your Name
Date: February 05, 2024
"""

from datetime import datetime
from adapters.dto.activity_id import ActivityIdDto
from adapters.enums.activity_status import ActivityStatus
from adapters.repositories.activity_repository import ActivityRepository

class ActivityGateway:
    def __init__(self, repository: ActivityRepository):
        self.repository = repository

    def create_activity(self, activity: ActivityIdDto):
        pass

    def get_activity_from_id(self, activity_id: int) -> ActivityIdDto | None:
        pass

    def get_activity_from_name(self, name: str) -> list[ActivityIdDto] | None:
        pass

    def get_activity_from_status(self, status: ActivityStatus) -> list[ActivityIdDto] | None:
        pass

    def get_activity_from_date(self, starting_date: datetime, final_date: datetime) -> list[ActivityIdDto] | None:
        pass

    def update_activity(self, activity: ActivityIdDto):
        pass

    def delete_activity(self, index: int):
        pass
