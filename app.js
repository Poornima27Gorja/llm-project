function uploadResume(event) {
  event.preventDefault(); // prevent form reload

  const email = document.getElementById("email").value;
  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const phone = document.getElementById("phone").value;
  const file = document.getElementById("resumeFile").files[0];

  if (!file || !email || !firstName || !lastName || !phone) {
    alert("Please fill all fields and upload a resume.");
    return;
  }

  const formData = new FormData();
  formData.append("email", email);
  formData.append("firstName", firstName);
  formData.append("lastName", lastName);
  formData.append("phone", phone);
  formData.append("resume", file);

  fetch("http://127.0.0.1:5000/upload-resume", {
  method: "POST",
  body: formData
})
  .then((res) => res.json())
  .then((data) => {
    if (data.result) {
      document.getElementById("output").innerText = data.result;
    } else if (data.error) {
      document.getElementById("output").innerText = "❌ Error: " + data.error;
    } else {
      document.getElementById("output").innerText = "❌ Unknown error occurred.";
    }
  })
  .catch((err) => {
    console.error("❌ Upload failed:", err);
    alert("Something went wrong. Check the console.");
  });
}
