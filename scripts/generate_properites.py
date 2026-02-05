import json
import os
from pathlib import Path

env = os.environ["ENV"].lower()
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]

raw_json = os.environ["INT_DETAILS_JSON"]

# Validate JSON
try:
    int_details = json.loads(raw_json)
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

int_details_string = json.dumps(int_details)

# File name based on env
file_name = f"{env}.properties"
file_path = Path(file_name)

content = f"""
env={env}
onboarding_project_Name={onboarding_project_name}
Job_name={job_name}
intDetails="{int_details_string}"
Remarks={remarks}
domain={domain}
project_Name={project_name}
""".strip()

with open(file_path, "w") as f:
    f.write(content)

print(f"{file_name} created successfully")
