def counseling(result):

    if result==1:
        return """
Student is at HIGH RISK.

Recommendations

• Academic Counseling
• Financial Support
• Parent Meeting
• Psychological Counseling
• Weekly Monitoring
"""
    else:
        return """
Student is SAFE.

Recommendations

• Encourage participation
• Career Guidance
• Continue Monitoring
"""
