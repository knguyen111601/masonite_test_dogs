""" A DoggiesController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Doggies import Doggies

class DoggiesController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", DoggiesController)
        """
        id = self.request.param("id")
        return Doggies.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", DoggiesController)
        """
        return Doggies.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", DoggiesController)
        """
        name = self.request.input("name")
        age = self.request.input("age")
        dog = Doggies.create({"name": name, "age": age})
        return dog


    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", DoggiesController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", DoggiesController)
        """

        pass