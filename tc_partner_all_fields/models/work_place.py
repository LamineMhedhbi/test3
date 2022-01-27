from odoo import models, fields


class WorkPlace(models.Model):
    _name = "work.place"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Work Place Name should be unique!")]

    name = fields.Char(string="Name")
