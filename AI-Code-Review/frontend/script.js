async function reviewCode() {

    const code = document.getElementById("codeInput").value;

    if (!code.trim()) {
        alert("Please enter some code.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    try {

        const response = await fetch(
            "https://ai-code-review-zzz1.onrender.com/review",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    code: code
                })
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        console.log("API Response:", data);

        updateList(
            "issues",
            data.issues || []
        );

        updateList(
            "suggestions",
            data.suggestions || []
        );

        document.getElementById("optimizedCode").innerText =
            data.optimized_code || "";

    }
    catch (error) {

        console.error(error);

        updateList(
            "issues",
            ["Failed to get review"]
        );

        updateList(
            "suggestions",
            []
        );

        document.getElementById("optimizedCode").innerText =
            "";
    }

    document.getElementById("loader").style.display = "none";
    document.getElementById("codeInput").style.border = "none";
    for (let i = 0; i < 3; i++) {
        document.getElementsByClassName("review-box")[i].style.border = "2px solid white";
    }
}

function updateList(id, items) {

    const list = document.getElementById(id);

    if (!items || items.length === 0) {
        list.innerHTML = "<li>None Found</li>";
        return;
    }

    list.innerHTML = items
        .map(item => `<li>${item}</li>`)
        .join("");
}
function copycode() {
    const code = document.getElementById("optimizedCode").innerText;

    navigator.clipboard.writeText(code);

    const btn = document.getElementById("copy");
    btn.textContent = "copied";

    setTimeout(function () {
        btn.textContent = "copy";

    }, 2000);
}
function clearcode(){
    document.getElementById("codeInput").value="";
    document.getElementById("issues").innerText = "";
}
const themeBtn = document.getElementById("themeToggle");

themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("lightmode");

    if (document.body.classList.contains("lightmode")) {
        themeBtn.textContent = "Dark Mode🌙";
    }
    else {
        themeBtn.textContent = "Light Mode☀️";
    }
});