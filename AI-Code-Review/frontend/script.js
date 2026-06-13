async function reviewCode() {

    const code = document.getElementById("codeInput").value;

    if (!code.trim()) {
        alert("Please enter some code.");
        return;
    }

    document.getElementById("loader").style.display = "block";


    const response = await fetch(
        "http://localhost:8000/review",
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
    const data = await response.json();
    document.getElementById("loader").style.display = "none";
    document.getElementById("score").innerText =
        data.score + "/10";

    updateList("issues", data.issues);

    updateList("suggestions", data.suggestions);

    document.getElementById("optimizedCode").innerText =
        data.optimized_code;
}
function updateList(id, items) {

    const list = document.getElementById(id);

    if (items.length === 0) {
        list.innerHTML = "<li>None Found</li>";
        return;
    }

    list.innerHTML = items.map(
        item => `<li>${item}</li>`
    ).join("");
}
