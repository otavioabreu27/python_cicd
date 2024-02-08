from adapters.enums.activity_status import ActivityStatus
from drivers.gateway.activity_gateway import ActivityGateway
from usecases.activity_usecase import ActivityUsecase


class CreateActivity(ActivityUsecase):
    def __init__(self, gateway: ActivityGateway):
        self.gateway = gateway

    def create(self, name: str, description: str, status: ActivityStatus):
        pass
