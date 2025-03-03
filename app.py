#!/usr/bin/env python3
import os

import aws_cdk as cdk

from vwds_project.vwds_project_stack import VWDSStack


app = cdk.App()

env = cdk.Environment(account="<ACCOUNT_NUMBER>", region="eu-central-1")  # Replace with your AWS Account ID & Region

VWDSStack(app, "VWDSStack", env=env)

app.synth()
