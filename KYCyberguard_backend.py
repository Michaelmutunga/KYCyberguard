# KYCyberGuard Flask Backend

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data to store assessments (in a real system, use a database)
assessments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/assess', methods=['POST'])
def assess():
    try:
        data = request.get_json()
        if not data or not isinstance(data, dict):
            raise ValueError("Invalid input data")
        
        company_name = data.get('company_name')
        cybersecurity_score = calculate_score(data)
        
        assessment = {
            "company_name": company_name,
            "score": cybersecurity_score,
            "recommendations": generate_recommendations(cybersecurity_score)
        }
        assessments.append(assessment)
        return jsonify({"status": "success", "assessment": assessment}), 200
    except ValueError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500


def calculate_score(data):
    score = 0
    if data.get('has_antivirus'):
        score += 20
    if data.get('has_firewall'):
        score += 20
    if data.get('has_ids'):
        score += 20
    if data.get('employee_training'):
        score += 20
    if data.get('data_backup'):
        score += 20
    return score


def generate_recommendations(score):
    if score < 60:
        return [
            "Implement antivirus software",
            "Set up a firewall",
            "Conduct regular employee cybersecurity training"
        ]
    elif score < 80:
        return ["Improve data backup policies", "Enhance intrusion detection systems"]
    else:
        return ["Maintain current cybersecurity practices"]

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

