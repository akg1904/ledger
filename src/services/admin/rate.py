from src.repository.postgresql.admin.rate import RateRepository


class RateService:

    def __init__(self):
        self.rate_repository = RateRepository()

    def get_by_i_code(self):

        response = self.rate_repository.get_rate()
        return response
