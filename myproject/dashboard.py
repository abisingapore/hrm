"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'abiweb.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Group: Administration & Applications'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
            ]
        ))
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Human Resource Manager'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',
                'insurance.models.*',
                'dash.models.*',
                'webform.models.Contract',
                'webform.models.EmploymentHistory',
                ),
        ))

        self.children.append(modules.AppList(
            _('Insurance Administration'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',
                'webform.models.*',
                'dash.models.*',
                'insurance.models.Report',
                ),
        ))

        self.children.append(modules.AppList(
            _('Dashboard'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',
                'webform.models.*',
                'insurance.models.*',
                'dash.models.Action',
                'dash.models.Candidates',
                ),
        ))


        self.children.append(modules.LinkList(
            layout='inline',
            column=3,
            children=(
                {
                    'title': 'ABI Website',
                    'url': 'http://www.abisingapore.com',
                    'external': True,
                    'description': 'ABI Singapore',
                },
                {
                    'title': 'ABI Facebook',
                    'url': 'http://www.abisingapore.com',
                    'external': True,
                    'description': 'ABI Singapore',
                },
                {
                    'title': 'ABI Twitter',
                    'url': 'http://www.abisingapore.com',
                    'external': True,
                    'description': 'ABI Singapore',
                },
                {
                    'title': 'ABI LinkedIn',
                    'url': 'http://www.abisingapore.com',
                    'external': True,
                    'description': 'ABI Singapore',
                },

            )
        ))
        
        # append an app list module for "Administration"

        # append another link list module for "support".

        
        # append another link list module for "support".

        
        # append a feed module

        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=13,
            collapsible=True,
            column=2,
        ))


