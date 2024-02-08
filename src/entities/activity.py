"""
activity.py

Author: Your Name
Date: February 05, 2024
"""

from datetime import datetime
from adapters.enums.activity_status import ActivityStatus

class Activity:
    """Test"""
    def __init__ (
        self,
        name: str,
        description: str,
        status: ActivityStatus,
        creation_date: datetime = datetime.now()
    ):
        self.name = name
        self.description = description
        self.status = status
        self.creation_date = creation_date

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_status(self) -> ActivityStatus:
        return self.status

    def get_creation_date(self) -> datetime:
        return self.creation_date
