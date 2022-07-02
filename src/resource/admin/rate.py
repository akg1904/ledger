from src.resource.base import BaseResource
from src.services.admin.rate import RateService


class RateResource(BaseResource):

    def get(self):
        rate_service = RateService()
        response = rate_service.get_by_i_code()
        return response
