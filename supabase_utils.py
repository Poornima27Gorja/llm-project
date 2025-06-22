import os
from dotenv import load_dotenv
from supabase import create_client

# ✅ Load environment variables right here
load_dotenv(dotenv_path=".env")

# ✅ Now fetch them
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# ✅ Debug check
print("✅ DEBUG - SUPABASE_URL:", url)
print("✅ DEBUG - SUPABASE_SERVICE_ROLE_KEY:", key)

# ✅ Handle missing keys
if not url or not key:
    raise Exception("❌ Environment variables not loaded. Check .env file.")

# ✅ Create Supabase client
supabase = create_client(url, key)

def save_to_supabase(first_name, last_name, phone, email, resume, role, questions):
    supabase.table("career_logs").insert({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email,
        "resume": resume,
        "advice": role,
        "questions": questions
    }).execute()

