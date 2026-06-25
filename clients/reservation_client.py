from .base_client import BaseClient


class ReservationClient(BaseClient):
    def create(self, created_item_id, data):
        data["item_id"] = created_item_id
        return self.post("/api/reservations/", json=data)

    def cancel(self, rid):
        return self.delete(f"/api/reservations/{rid}")
