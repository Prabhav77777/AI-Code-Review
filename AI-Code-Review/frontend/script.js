async function reviewCode() {

    const code = document.getElementById("codeInput").value;

    if (!code.trim()) {
        alert("Please enter some code.");
        return;
    }

    // Show loading animation
    const loading = document.getElementById("loading");
    const reviewBtn = document.getElementById("review");

    loading.style.display = "flex";
    reviewBtn.disabled = true;
    reviewBtn.innerText = "Reviewing...";

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

        updateList("issues", data.issues || []);
        updateList("suggestions", data.suggestions || []);

        document.getElementById("optimizedCode").innerText =
            data.optimized_code || "";

    } catch (error) {

        console.error(error);

        updateList("issues", ["Failed to get review"]);
        updateList("suggestions", []);
        document.getElementById("optimizedCode").innerText = "";

    } finally {

        // Hide loading animation
        loading.style.display = "none";
        reviewBtn.disabled = false;
        reviewBtn.innerText = "Review Code";

        document.getElementById("codeInput").style.border = "none";

        const boxes = document.getElementsByClassName("review-box");
        for (let i = 0; i < boxes.length; i++) {
            boxes[i].style.border = "2px solid var(--w)";
        }
    }
}

function updateList(id, items) {

    const list = document.getElementById(id);

    if (!items || items.length === 0) {
        list.innerHTML = "<li>None Found</li>";
        return;
    }

    list.innerHTML = items.map(item => `<li>${item}</li>`).join("");
}

function copycode() {

    const code = document.getElementById("optimizedCode").innerText;

    navigator.clipboard.writeText(code);

    const btn = document.getElementById("copy");
    btn.textContent = "Copied";

    setTimeout(() => {
        btn.textContent = "Copy";
    }, 2000);
}
function clearcode() {

    document.getElementById("codeInput").value = "";
    document.getElementById("issues").innerHTML = "";
    document.getElementById("suggestions").innerHTML = "";
    document.getElementById("optimizedCode").innerText = "";

    document.getElementById("codeInput").style.border = "2px solid var(--w)";

    const boxes = document.getElementsByClassName("review-box");
    for (let i = 0; i < boxes.length; i++) {
        boxes[i].style.border = "none";
    }
}

function redmode() {
    document.body.className = "red";
}


