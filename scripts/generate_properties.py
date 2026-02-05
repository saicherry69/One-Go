import os
import json
import base64

raw_b64 = os.environ.get("INT_DETAILS_JSON_B64")

if not raw_b64:
    raise Exception("INT_DETAILS_JSON_B64 is missing")

try:
    decoded_json = base64.b64decode(raw_b64).decode("utf-8")
    int_details = json.loads(decoded_json)
except Exception as e:
    raise Exception(f"Invalid JSON input after base64 decode: {e}")

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
