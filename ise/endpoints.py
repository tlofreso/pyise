from ise import exceptions


class Endpoints(object):
    def __init__(self, ise_con):
        self.ise_con = ise_con

    def get_by_mac(self, mac=None, **kwargs):
        # Return details of endpoint by MAC

        return self.ise_con.get("/endpoint?filter=mac.EQ." + mac, **kwargs)

    def get_groups(self, **kwargs):
        # Return all identity groups

        return self.ise_con.get("/endpointgroup", **kwargs)

    def get_endpoints(self, **kwargs):
        # Return all endpoints

        return self.ise_con.get("/endpoint", **kwargs)

    def create_endpoint(self, name, description, mac, groupID, staticGroupAssignment):

        data = {"ERSEndPoint" : {"name" : name,
                    "description" : description,
                    "mac" : mac,
                    "groupId" : groupID,
                    "staticGroupAssignment" : staticGroupAssignment
                  },
                }
        
        return self.ise_con.post("/endpoint", data, **kwargs)

    def update_endpoint(self, mac=None, **kwargs):

        return self.ise_con.put("/endpoint" + mac, **kwargs)

    def delete_endpoint():
        pass






