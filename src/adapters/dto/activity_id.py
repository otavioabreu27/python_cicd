from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from adapters.enums.activity_status import ActivityStatus

@dataclass(frozen=True)
class ActivityIdDto:
    '''The DTO Class for Gateway, Repository and Usecase communication'''
    id: Optional[int] = None
    name: str
    description: str
    status: ActivityStatus
    creation_date: Optional[datetime] = datetime.now()
