from config import Config
from .base_client import BaseClient


class ItemClient(BaseClient):
    def create(self, wid, data):
        print(f"{Config.JWT_TOKEN}")
        print(wid, data)
        r = self.post(f"/api/wishlists/{wid}/items/", data=data, headers={
            "Authorization":f"Bearer {Config.JWT_TOKEN}"
        })
        print(r.text)
        return r

    def list(self, wid):
        return self.get(f"/api/wishlists/{wid}/items/")

    def update(self, wid, iid, data):
        return self.patch(f"/api/wishlists/{wid}/items/{iid}", json=data)

    def delete_one(self, wid, iid):
        return self.delete(f"/api/wishlists/{wid}/items/{iid}")

    def list_pub(self, wid):
        return self.get(f"/api/wishlists/{wid}/items/public")
    
    def reorder(self, wid, data):
        return self.post(f"/api/wishlists/{wid}/items/reorder", files=data)