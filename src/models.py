class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

        # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return "" #random.randint(0, 99999999) //import random 

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members