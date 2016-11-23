# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    responsible_employee_ids = fields.Many2many('hr.employee', 'project_task_employee_rel', 'task_id', 'employee_id',
                                                'Responsible Employee')
