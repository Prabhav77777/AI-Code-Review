async function reviewCode(){

    const code =
    document.getElementById("codeInput").value;

    const response =
    await fetch(
        "http://localhost:8000/review",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({code})
        }
    );

    const data =
    await response.json();

    document.getElementById("output")
        .innerText = data.review;
}
