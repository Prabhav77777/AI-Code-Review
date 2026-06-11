// function updateList(id, items){
//     const list=document.getElementById(id);

//     if(items.length===0){
//         list.innerHTML="<li>None Found</li>";
//         return;
//     }
//     document.body.textContent

//     list.innerHTML=items.map(item=>`<li>${item}</li>`).join("");
// }   

// async function reviewCode(){

//     const code=document.getElementById("codeInput").value;
//     const language=document.getElementById("language").value;

//     if(!code.trim()){
//         alert("Please enter code.");
//         return;
//     }

//     document.getElementById("loading").style.display="block";

//     try{

//         /*
//         Replace URL with FastAPI backend
//         */

//         const response=await fetch(
//             "http://localhost:8000/review",
//             {
//                 method:"POST",
//                 headers:{
//                     "Content-Type":"application/json"
//                 },
//                 body:JSON.stringify({
//                     code,
//                     language
//                 })
//             }
//         );

//         const data=await response.json();

//         document.getElementById("score").innerText=data.score;

//         updateList("bugs",data.bugs);
//         updateList("security",data.security);
//         updateList("performance",data.performance);
//         updateList("bestPractices",data.suggestions);

//     }
//     catch(error){

//         console.error(error);

//         document.getElementById("score").innerText="85";

//         updateList("bugs",[
//             "Possible null reference detected"
//         ]);

//         updateList("security",[
//             "Input validation missing"
//         ]);

//         updateList("performance",[
//             "Use direct iteration instead of indexing"
//         ]);

//         updateList("bestPractices",[
//             "Improve variable naming"
//         ]);
//     }

//     document.getElementById("loading").style.display="none";
// }
