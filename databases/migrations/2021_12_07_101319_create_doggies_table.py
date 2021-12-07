"""CreateDoggiesTable Migration."""

from masoniteorm.migrations import Migration


class CreateDoggiesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("doggies") as table:
            table.increments("id")
            table.integer("owner_id").unsigned()
            table.foreign("owner_id").references("id").on("owners")
            table.string("name")
            table.integer("age")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("doggies")
        

