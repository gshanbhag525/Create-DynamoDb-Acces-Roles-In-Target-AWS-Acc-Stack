import aws_cdk as core
import aws_cdk.assertions as assertions

from create_db_acces_roles_in_target_acc.create_db_acces_roles_in_target_acc_stack import CreateDbAccesRolesInTargetAccStack

# example tests. To run these tests, uncomment this file along with the example
# resource in create_dej_acces_roles_in_target_acc/create_dej_acces_roles_in_target_acc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CreateDbAccesRolesInTargetAccStack(app, "create-db-acces-roles-in-target-acc")
    template = assertions.Template.from_stack(stack)
