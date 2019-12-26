from ise import exceptions


class Endpoints(object):
    def __init__(self, ise_con):
        self.ise_con = ise_con

    def get_by_mac(self, mac=None, **kwargs):
        """GET an endpoint by MAC address

        :param mac: specify a MAC address. Format: mac='00:00:00:00:00:00'
        :param kwargs: requests body dict
        """

        return self.ise_con.get("/endpoint?filter=mac.EQ." + mac, **kwargs)

    def get_groups(self, api_filter=None, **kwargs):
        """GET all Endpoint Identity Groups

        :param api_filter: Apply a filter to GET call. Format: api_filter='?page=1&size=10'
        :param kwargs: requests body dict
        """

        return self.ise_con.get("/endpointgroup", api_filter, **kwargs)

    def get_endpoints(self, **kwargs):
        # Return all endpoints

        return self.ise_con.get("/endpoint", **kwargs)

    def create_endpoint(
        self, name, description, mac, groupID, staticGroupAssignment, **kwargs
    ):
        # Create an endpoint that does not yet exits

        data = {
            "ERSEndPoint": {
                "name": name,
                "description": description,
                "mac": mac,
                "groupId": groupID,
                "staticGroupAssignment": staticGroupAssignment,
            }
        }

        return self.ise_con.post("/endpoint", data, **kwargs)

    def update_endpoint(
        self, name, description, groupID, staticGroupAssignment, mac=None, **kwargs
    ):
        # Update an existing endpoint

        data = {
            "ERSEndPoint": {
                "name": name,
                "description": description,
                "mac": mac,
                "groupId": groupID,
                "staticGroupAssignment": staticGroupAssignment,
            }
        }

        return self.ise_con.put("/endpoint" + mac, **kwargs)

    def delete_endpoint():
        pass

