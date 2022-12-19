from aws_cdk import Duration, Stack, CfnOutput
from constructs import Construct
import aws_cdk.aws_dynamodb as dynamodb
from aws_cdk.aws_iam import (
    Policy,
    ManagedPolicy,
    PolicyStatement,
    Effect,
    Role,
    AccountPrincipal,
    CompositePrincipal,
)

from create_db_acces_roles_in_target_acc.config import config


class CreateDbAccesRolesInTargetAccStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        account_id = self.account
        region = self.region

        # policy to access target db from main acc
        access_target_db_policy = ManagedPolicy(
            self,
            id="access_target_db_policy",
            statements=[
                PolicyStatement(
                    effect=Effect.ALLOW,
                    actions=[
                        "dynamodb:BatchGetItem",
                        "dynamodb:BatchWriteItem",
                        "dynamodb:PutItem",
                        "dynamodb:PartiQLSelect",
                        "dynamodb:GetItem",
                        "dynamodb:PartiQLInsert",
                        "dynamodb:Scan",
                        "dynamodb:Query",
                    ],
                    resources=[
                        f"arn:aws:dynamodb:{config['TARGET_ACC_REGION']}:{config['TARGET_ACC_ID']}:table/{config['TARGET_ACC_TABLE_NAME']}/index/*",
                        f"arn:aws:dynamodb:{config['TARGET_ACC_REGION']}:{config['TARGET_ACC_ID']}:table/{config['TARGET_ACC_TABLE_NAME']}",
                        f"arn:aws:dynamodb:{config['TARGET_ACC_REGION']}:{config['TARGET_ACC_ID']}:table/{config['TARGET_ACC_HMS_TABLE_NAME']}/index/*",
                        f"arn:aws:dynamodb:{config['TARGET_ACC_REGION']}:{config['TARGET_ACC_ID']}:table/{config['TARGET_ACC_HMS_TABLE_NAME']}",
                    ],
                )
            ],
        )

        principal = []
        principal.append(AccountPrincipal(config["MAIN_ACC_ID"]))
        composite_principal = CompositePrincipal(*principal)

        target_db_access_role = Role(
            self,
            id="target_db_access_role",
            role_name=config["desired_target_account_role_name"],
            assumed_by=composite_principal,
            description="target db role to be used by main acc lambda",
        )

        access_target_db_policy.attach_to_role(target_db_access_role)
