import os
import json
from pathlib import Path

env = os.environ["ENV"]
remarks = os.environ["REMARKS"]
domain = os.environ["DOMAIN"]
project_name = os.environ["PROJECT_NAME"]
onboarding_project_name = os.environ["ONBOARDING_PROJECT_NAME"]
job_name = os.environ["JOB_NAME"]

raw_json = os.environ["INT_DETAILS_JSON"]

# 🔥 CRITICAL FIX: strip leading/trailing whitespace
raw_json = raw_json.strip()

try:
    int_details = json.loads(raw_json)
except json.JSONDecodeError as e:
    raise Exception(f"Invalid JSON input: {e}")

int_details_string = json.dumps(int_details, separators=(",", ":"))

content = f"""env={env}
onboarding_project_Name={onboarding_project_name}
Job_name={job_name}
intDetails={int_details_string}
Remarks={remarks}
domain={domain}
project_Name={project_name}
"""

Path(f"{env}.properties").write_text(content)

print(f"✅ {env}.properties generated successfully")
