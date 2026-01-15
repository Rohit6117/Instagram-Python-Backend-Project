document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("registerForm");
    const API = "http://127.0.0.1:8000";

    // Get DOM elements
    const user_name = document.getElementById("user_name");
    const user_email = document.getElementById("user_email");
    const user_fullname = document.getElementById("user_fullname");
    const user_phone = document.getElementById("user_phone");
    const user_gender = document.getElementById("user_gender");
    const user_dob = document.getElementById("user_dob");
    const user_bio = document.getElementById("user_bio");
    const user_password = document.getElementById("user_password");
    const captcha_text = document.getElementById("captcha_text");

    loadCaptcha();

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const user = {
            user_name: user_name.value.trim(),
            user_email: user_email.value.trim(),
            user_fullname: user_fullname.value.trim(),
            user_phone: user_phone.value.trim(),
            user_gender: user_gender.value,
            user_dob: user_dob.value,
            user_bio: user_bio.value.trim(),
            user_password: user_password.value
        };

        const captcha = {
            captcha_text: captcha_text.value.trim()
        };

        if (Object.values(user).some(v => !v) || !captcha.captcha_text) {
            alert("Please fill all required fields!");
            return;
        }

        try {
            const res = await fetch(`${API}/auth/user`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, captcha })
            });

            const data = await res.json();

            if (!res.ok || data.success === false) {
                alert(data.message || "Invalid captcha");
                loadCaptcha();
                return;
            }

            alert("Account created successfully!");
            window.location.href = "login.html";

        } catch (err) {
            console.error(err);
            alert("Server error!");
        }
    });
});

async function loadCaptcha() {
    const API = "http://127.0.0.1:8000";

    try {
        const res = await fetch(`${API}/auth/register/captcha`);
        const data = await res.json();

        document.getElementById("captchaText").textContent = data.captcha_text;

    } catch (err) {
        console.error("Error loading captcha:", err);
        document.getElementById("captchaText").textContent = "Error!";
    }
}
