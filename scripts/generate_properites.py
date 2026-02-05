import json
import os
from pathlib import Path

env = os.environ["ENV"]
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]
file_path = os.environ["FILE_PATH"]

raw_json = os.environ["INT_DETAILS_JSON"]

try:
    int_details = json.loads(raw_json)
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

int_details_string = json.dumps(int_details)

content = f"""
env={env}
onboarding_project_Name={onboarding_project_name}
Job_name={job_name}
intDetails="{int_details_string}"
Remarks={remarks}
domain={domain}
project_Name={project_name}
""".strip()

path = Path(file_path)
path.parent.mkdir(parents=True, exist_ok=True)

with open(path, "w") as f:
    f.write(content)

print(f"Properties file created at {file_path}")
