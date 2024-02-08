from adapters.dto.activity_id import ActivityIdDto
from entities.activity import Activity


class ActivityUsecase:
    @staticmethod
    def activity_to_dto(activity: Activity) -> ActivityIdDto:
        return ActivityIdDto(
            name=activity.get_name(),
            description=activity.get_description(),
            status=activity.get_status().value,
            creation_date=activity.get_creation_date()
        )
