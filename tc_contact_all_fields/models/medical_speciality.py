from odoo import models, fields


class MedicalSpeciality(models.Model):
    _name = "medical.speciality"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Medical Speciality Name should be unique!")]

    name = fields.Char(string="Medical Speciality")
