import os
import json
from pathlib import Path

# Read simple inputs from env vars
env = os.environ["ENV"]
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]

# Read integration JSON from file
json_path = Path("int_details.json")

if not json_path.exists():
    raise Exception("int_details.json file not found")

try:
    with open(json_path, "r", encoding="utf-8") as f:
        int_details = json.load(f)
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

# Convert JSON object to single-line string for properties file
int_details_string = json.dumps(int_details, separators=(",", ":"))

# Create properties file
file_name = f"{env}.properties"
file_path = Path(file_name)

content = f"""env={env}
onboarding_project_Name={onboarding_project_name}
Job_name={job_name}
intDetails="{int_details_string}"
Remarks={remarks}
domain={domain}
project_Name={project_name}
"""

file_path.write_text(content)

print(f"{file_name} created successfully")
