from adapters.enums.activity_status import ActivityStatus
from drivers.gateway.activity_gateway_sqlite import ActivityGatewaySqlite
from entities.activity import Activity
from usecases.create_activity import CreateActivity


class CreateActivitySqlite(CreateActivity):
    def __init__(self, gateway: ActivityGatewaySqlite):
        super().__init__(gateway)

    def create(self, name: str, description: str, status: ActivityStatus):
        activity = Activity(
            name,
            description,
            status,
        )

        try:
            self.gateway.create_activity(self.activity_to_dto(activity))
        except Exception as e:
            print(e)
