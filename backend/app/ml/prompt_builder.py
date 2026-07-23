def build_rca_prompt(analytics: dict, clusters: list) -> str:
    return f"""
You are an SRE and DevOps expert.

Analyze the following incident.

Incident Analytics:
{analytics}

Error Clusters:
{clusters}

Provide:

1. Executive Summary
2. Probable Root Cause
3. Impacted Services
4. Severity (Low/Medium/High/Critical)
5. Recommended Fixes
6. Preventive Measures

Return the response in Markdown.
"""