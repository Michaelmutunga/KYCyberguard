// Import necessary modules
const express = require('express');
const cors = require('cors');

// Initialize the Express application
const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Function to calculate assessment score and recommendations
function assessCompany(data) {
    let score = 0;
    const recommendations = [];

    // Scoring criteria
    if (data.has_antivirus) {
        score += 20;
    } else {
        recommendations.push("Install antivirus software to protect against malware.");
    }

    if (data.has_firewall) {
        score += 20;
    } else {
        recommendations.push("Implement a firewall to monitor and control network traffic.");
    }

    if (data.has_ids) {
        score += 20;
    } else {
        recommendations.push("Set up an Intrusion Detection System (IDS) to detect potential threats.");
    }

    if (data.employee_training) {
        score += 20;
    } else {
        recommendations.push("Conduct regular cybersecurity training for employees.");
    }

    if (data.data_backup) {
        score += 20;
    } else {
        recommendations.push("Establish a regular data backup strategy.");
    }

    return { score, recommendations };
}

// API route
app.post('/api/assess', (req, res) => {
    const { company_name, has_antivirus, has_firewall, has_ids, employee_training, data_backup } = req.body;

    if (!company_name || typeof company_name !== 'string') {
        return res.status(400).json({ message: "Invalid or missing 'company_name'." });
    }

    const assessment = assessCompany({
        has_antivirus,
        has_firewall,
        has_ids,
        employee_training,
        data_backup
    });

    return res.json({
        assessment: {
            company_name,
            score: assessment.score,
            recommendations: assessment.recommendations
        }
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

