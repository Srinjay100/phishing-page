from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import re
import requests

app = Flask(__name__)

# Enable CORS to allow communication with React frontend
from flask_cors import CORS
CORS(app)

# List of known phishing keywords or patterns
PHISHING_KEYWORDS = [
    "urgent", "account", "verify", "suspend", "password", "update", "security", "login",
    "Account Suspended", "Verify Your Account", "Immediate Action Required", "Suspicious Activity",
    "Password Expiry", "Reset Password", "Account Locked", "Unusual Login Attempt", "Security Alert",
    "Your Account is Compromised", "Limited Time Offer", "Verify Identity", "Click Here",
    "Sign In Now", "Urgent Notification", "Suspicious Logins Detected", "Unauthorized Access",
    "Confirm Your Email", "Security Code", "Update Your Information", "Please Respond",
    "Your Account Has Been Hacked", "Suspicious Activity Detected", "Action Required",
    "Verify Your Identity", "Immediate Attention Needed", "Account Verification",
    "Your Account is on Hold", "Payment Pending", "Refund Processed", "Important Message from",
    "Access Your Account", "Limited Time Only", "Request for Personal Information",
    "Account Verification Required", "Security Check", "Update Your Password",
    "Act Now to Avoid Suspension", "Claim Your Prize", "Free Gift", "Exclusive Offer",
    "Confirm Payment Details", "Confirm Personal Information", "Financial Information Needed",
    "Update Billing Information", "Activate Your Account", "Login From Unknown Location",
    "Transaction Alert", "Verify Your Credit Card", "Unusual Activity on Your Account"
]

def contains_phishing_keywords(text):
    text = text.lower()
    for keyword in PHISHING_KEYWORDS:
        if keyword in text:
            return True
    return False

def extract_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = []
    for a_tag in soup.find_all('a', href=True):
        urls.append(a_tag['href'])
    return urls

def analyze_email_content(email_text):
    warnings = []
    # Check for phishing keywords
    if contains_phishing_keywords(email_text):
        warnings.append("The email contains potential phishing keywords.")
    
    # Extract URLs
    urls = re.findall(r'http[s]?://\S+', email_text)
    if '<html>' in email_text.lower():
        urls.extend(extract_urls(email_text))

    # Return analysis results
    return {"warnings": warnings, "urls": urls}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    email_content = data.get("emailContent", "")
    if not email_content:
        return jsonify({"error": "Email content is empty"}), 400

    # Analyze the email content
    result = analyze_email_content(email_content)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
