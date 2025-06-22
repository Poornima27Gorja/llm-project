import os
import PyPDF2
import docx
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_logic import parse_resume, generate_questions
from supabase_utils import save_to_supabase
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()

# 🚀 Initialize Flask app
app = Flask(__name__)

# ✅ Enable CORS only for frontend (Live Server on port 5500)
CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5500"])

# 📄 Extract text from uploaded file
def extract_text_from_file(file):
    if file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.filename.endswith(('.docx', '.doc')):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

# 🔁 API route to handle uploaded form
@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    try:
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        phone = request.form["phone"]
        email = request.form["email"]
        file = request.files.get("resume")

        if file is None:
            return jsonify({"error": "No resume file uploaded"}), 400

        resume_text = extract_text_from_file(file)

        if not resume_text.strip():
            return jsonify({"error": "Could not extract text from the resume file"}), 400

        # ✅ Only print after resume_text is extracted safely
        print("📥 Received:", first_name, last_name, phone, email)
        print("📄 Resume Text (preview):", resume_text[:200])

        # 🧠 AI logic
        job_role = parse_resume(resume_text)
        questions = generate_questions(job_role)

        # 💡 Full advice to return
        full_advice = f"Suggested Role: {job_role}\n\nQuestions:\n{questions}"

        # 💾 Save to Supabase
        save_to_supabase(first_name, last_name, phone, email, resume_text, job_role, questions)

        return jsonify({"result": full_advice})

    except Exception as e:
        print("❌ Server error:", str(e))
        return jsonify({"error": str(e)}), 500

# ▶️ Start server
if __name__ == "__main__":
    app.run(debug=True)
