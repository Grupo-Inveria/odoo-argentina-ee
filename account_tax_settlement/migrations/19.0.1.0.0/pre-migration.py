# Copyright 2025 ADHOC SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Migration script from Odoo 18 to Odoo 19 for account_tax_settlement module.

    Key changes:
    - Updated read_group() to _read_group() with new signature
    - Ensured compatibility with Odoo 19 ORM changes
    """
    pass
