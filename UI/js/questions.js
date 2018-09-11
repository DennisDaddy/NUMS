
// this function creates a question
function getquestions(){
    fetch('https://gully.herokuapp.com/api/v1/questions',{
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then((res) => res.json())
    .then((data) => {
        let output = '<h2>Questions</h2>';
        data.forEach(function(data){
            output += `
            <div>
            <h3>${$data.title}</h3>
            </div>`;
        });
        document.getElementById('output').innerHTML = output;
    })
}

// // get all questions
// function getquestions(){

// }

// this function retieves a question details
function retrievequestion(){

}

// this function modifies a question
function editquestion(){

}

// this function deletes a question
function deletequestion(){

}