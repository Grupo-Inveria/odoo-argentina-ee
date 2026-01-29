# Copyright 2025 ADHOC SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Migration script from Odoo 18 to Odoo 19 for l10n_ar_account_tax_settlement module.

    Key changes:
    - Updated read_group() to _read_group() with new signature in wizards
    - Removed backward compatibility code for v16->v18 migrations
    - Activated ARBA changes for post-March 2026 specifications
    - Simplified code removing temporary workarounds (PR #743 reverts)
    - Ensured compatibility with Odoo 19 ORM changes
    """
    # No data migration needed, only code changes
    pass
