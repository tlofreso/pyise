from ise import exceptions


class Endpoints(object):
    def __init__(self, ise_con):
        self.ise_con = ise_con

    def get_endpoints_by_mac(self, mac, **kwargs):
        # Return details of endpoint by MAC

        return self.ise_con.get("/endpoint?filter=mac.EQ." + mac, mac=mac, **kwargs)

    def get_groups(self, **kwargs):
        # Return all identity groups

        return self.ise_con.get("/identitygroup", **kwargs)

    def get_endpoints(self, **kwargs):
        # Return all endpoints
        pass

    def create_endpoint():
        pass

    def update_endpoint():
        pass

    def delete_endpoint():
        pass
