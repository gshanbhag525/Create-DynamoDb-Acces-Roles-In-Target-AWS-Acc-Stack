#!/usr/bin/env python3
import os

import aws_cdk as cdk

from create_db_acces_roles_in_target_acc.create_db_acces_roles_in_target_acc_stack import (
    CreateDbAccesRolesInTargetAccStack,
)

app = cdk.App()
CreateDbAccesRolesInTargetAccStack(
    app,
    "CreateDbAccesRolesInTargetAccStack",
)

app.synth()
