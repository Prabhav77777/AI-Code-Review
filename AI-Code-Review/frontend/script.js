async function reviewCode() {

    const code = document.getElementById("codeInput").value;

    if (!code.trim()) {
        alert("Please enter some code.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    try {

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

        document.getElementById("output").innerText =
            data.review;

    }
    catch (error) {

        document.getElementById("output").innerText =
            "Error connecting to backend.";

        console.error(error);
    }

    document.getElementById("loader").style.display = "none";
}