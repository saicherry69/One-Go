import os
import json
from pathlib import Path

env = os.environ["ENV"]
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]

raw_json = os.environ["INT_DETAILS_JSON"].strip()

if (raw_json.startswith("'") and raw_json.endswith("'")) or \
   (raw_json.startswith('"') and raw_json.endswith('"')):
    raw_json = raw_json[1:-1].strip()


# 1️⃣ Validate JSON
try:
    int_details = json.loads(raw_json)
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

# 2️⃣ Convert JSON → string with escaped quotes & slashes
json_string = json.dumps(int_details)
json_string = json_string.replace("\\", "\\\\").replace('"', '\\"')

# 3️⃣ Wrap exactly as expected: ' " {...} " '
int_details_value = f"'\"{json_string}\"'"

# 4️⃣ Build properties content (quotes exactly like expected)
content = f"""env={env},
onboarding_project_Name='{onboarding_project_name}'
Job_name='{job_name}'
intDetails={int_details_value}
Remarks='{remarks}'
domain='{domain}'
project_Name='{project_name}'
"""

# 5️⃣ Write file
file_path = Path(f"{env}.properties")
file_path.write_text(content)

print(f"✅ {file_path.name} generated with escaped intDetails")
