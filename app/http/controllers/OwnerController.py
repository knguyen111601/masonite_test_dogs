""" A OwnerController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Owner import Owner

class OwnerController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", OwnerController)
        """
        id = self.request.param('id')
        return Owner.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", OwnerController)
        """
        return Owner.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", OwnerController)
        """
        dog_id = self.request.input("dog_id")
        name = self.request.input("name")
        owner = Owner.create({"name": name, "dog_id": dog_id})
        return owner

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", OwnerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", OwnerController)
        """

        pass