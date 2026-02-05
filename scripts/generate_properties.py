import os
import json
from pathlib import Path

# Read inputs from environment
env = os.environ["ENV"]
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]

# Read JSON file written by workflow
json_file = Path("int_details.json")

try:
    int_details = json.loads(json_file.read_text())
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

# Convert JSON to single-line string
int_details_string = json.dumps(int_details)

# Create properties content
content = f"""env={env}
onboarding_project_Name={onboarding_project_name}
job_name={job_name}
domain={domain}
project_name={project_name}
remarks={remarks}
intDetails={int_details_string}
"""

# Write properties file
output_file = Path(f"{env}.properties")
output_file.write_text(content)

print(f"✅ {output_file.name} generated successfully")

