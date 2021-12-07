"""CreateOwnersTable Migration."""

from masoniteorm.migrations import Migration


class CreateOwnersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("owners") as table:
            table.increments("id")
            table.string("name")
            table.integer("dog_id")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("owners")

    
