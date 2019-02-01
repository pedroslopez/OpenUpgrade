# Copyright 2019 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def fill_purchase_order_user_id(cr):
    cr.execute(
        """
        UPDATE purchase_order
        SET user_id = create_uid
        WHERE user_id IS NULL
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    fill_purchase_order_user_id(env.cr)
    openupgrade.load_data(
        env.cr, 'purchase', 'migrations/12.0.1.2/noupdate_changes.xml')
    openupgrade.delete_records_safely_by_xml_id(
        env, [
            'purchase.mail_template_data_notification_email_purchase_order',
        ],
    )
