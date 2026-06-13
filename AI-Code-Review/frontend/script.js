require.config({
    paths:{
        vs:"https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function(){

    window.editor = monaco.editor.create(
        document.getElementById("editor"),
        {
            value:`print("Hello World")`,
            language:document.getElementById("language").value,
            theme:"vs-dark",
            automaticLayout:true,
            minimap:{
                enabled:false
            }
        }
    );

});

async function reviewCode(){

    document.getElementById("loader").style.display = "block";

    const code = editor.getValue();

    try{

        const response = await fetch(
            "http://localhost:8000/review",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({code})
            }
        );

        const data = await response.json();

        document.getElementById("output").innerText =
        data.review;

    }
    catch(error){

        document.getElementById("output").innerText =
        "Error connecting to backend.";

        console.error(error);
    }

    document.getElementById("loader").style.display = "none";
}