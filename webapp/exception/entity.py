class EntityError(Exception):
    entity_name: str
    entity_id: int
    detail: str


class EntityNotFoundError(EntityError):
    def __init__(self, entity_name, entity_id):
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.detail = f"{self.entity_name} with id: {self.entity_id} not found"
        super().__init__(self.detail)


class EntityValueError(EntityError):
    def __init__(self, entity_name, entity_id, detail):
        self.entity_name = entity_name
        self.entity_id = entity_id

        self.detail = f"{self.entity_name} with id: {self.entity_id} has error: {detail}"
        super().__init__(self.detail)
