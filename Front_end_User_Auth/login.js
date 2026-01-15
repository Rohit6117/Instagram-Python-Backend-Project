// function login() {
//     const userId = document.getElementById("user_id").value;
//     const password = document.getElementById("password").value;

//     if (!userId || !password) {
//         document.getElementById("error").textContent = "All fields are required";
//         return;
//     }

//     // Backend API example

//     fetch("http://127.0.0.1:8000/auth/login", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({
//             user_id: userId,
//             user_password: password
//         })
//     })
    

//     alert("Login successful");
//     document.getElementById("error").textContent = "";
// }
function login() {
    const userId = document.getElementById("user_id").value;
    const password = document.getElementById("password").value;

    if (!userId || !password) {
        document.getElementById("error").textContent = "All fields are required";
        return;
    }

    const formData = new URLSearchParams();
    formData.append("username", userId);   // IMPORTANT
    formData.append("password", password);

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData.toString()
    })
    .then(res => res.json())
    .then(data => {
        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "dashboard.html";
        } else {
            document.getElementById("error").textContent = "Invalid credentials";
        }
    })
    .catch(() => {
        document.getElementById("error").textContent = "Server error";
    });
}
