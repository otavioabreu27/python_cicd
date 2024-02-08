from datetime import datetime
from adapters.dto.activity_id import ActivityIdDto
from adapters.enums.activity_status import ActivityStatus
from adapters.repositories.activity_repository_sqlite import ActivityRepositorySqlite
from drivers.gateway.activity_gateway import ActivityGateway

class ActivityGatewaySqlite(ActivityGateway):
    """Activity Gateway Implementation for SQLite"""
    def __init__(self, repository: ActivityRepositorySqlite):
        super().__init__(repository)

    def create_activity(self, activity: ActivityIdDto):
        try:
            self.repository.insert_activity(
               activity.name,
               activity.description,
               activity.status,
               activity.creation_date
            )
        except Exception as e:
            print(e)

    def get_activity_from_id(self, activity_id: int) -> ActivityIdDto | None:
        try:
            result = self.repository.fetch_from_id(activity_id)
            if result:
                activity = ActivityIdDto(
                    result[0],
                    result[1],
                    result[2],
                    ActivityStatus(result[3]),
                    datetime.strptime(result[4], "%Y-%m-%d")
                )

                return activity
        except Exception as e:
            print(e)

        return None

    def get_activity_from_name(self, name: str) -> list[ActivityIdDto] | None:
        try:
            result = self.repository.fetch_from_name(name)
            if result:
                activity = ActivityIdDto(
                    result[0],
                    result[1],
                    result[2],
                    ActivityStatus(result[3]),
                    datetime.strptime(result[4], "%Y-%m-%d") 
                )

                return activity
        except Exception as e:
            print(e)
        
        return None

    def get_activity_from_status(self, status: ActivityStatus) -> list[ActivityIdDto] | None:
        try:
            result = self.repository.fetch_from_status(ActivityStatus.value)
            if result:
                activity = ActivityIdDto(
                    result[0],
                    result[1],
                    result[2],
                    ActivityStatus(result[3]),
                    datetime.strptime(result[4], "%Y-%m-%d")
                )

                return activity
        except Exception as e:
            print(e)

        return None

    def get_activity_from_date(
            self, starting_date: datetime, final_date: datetime
    ) -> list[ActivityIdDto] | None:
        try:
            result = self.repository.fetch_from_date(starting_date, final_date)
            if result:
                activity = ActivityIdDto(
                    result[0],
                    result[1],
                    result[2],
                    ActivityStatus(result[3]),
                    datetime.strptime(result[4], "%Y-%m-%d")
                )

                return activity
        except Exception as e:
            print(e)

        return None

    def update_activity(self, activity: ActivityIdDto):
        try:
            self.repository.update_activity(
                activity.id,
                activity.name,
                activity.description,
                activity.status.value
            )
        except Exception as e:
            print(e)

    def delete_activity(self, index: int):
        try:
            self.delete_activity(index)
        except Exception as e:
            print(e)
