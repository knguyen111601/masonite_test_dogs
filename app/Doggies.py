"""Doggies Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Doggies(Model):
    """Doggies Model."""
    @has_many("owner_id", "id")
    def owners(self):
        from app.Owner import Owner
        return Owner
    __table__= "doggies"