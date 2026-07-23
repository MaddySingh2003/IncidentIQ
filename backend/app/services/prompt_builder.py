def build_prompt(analytics, clusters):

    return f"""
You are an experienced Site Reliability Engineer.

Analyze the following production incident.

Analytics

{analytics}

Error Clusters

{clusters}

Generate:

1. Executive Summary

2. Root Cause

3. Severity

4. Impacted Services

5. Business Impact

6. Immediate Fix

7. Long-term Prevention

Respond in markdown.
"""