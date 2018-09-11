
// let route = "https://gully.herokuapp.com/api/v1";
// fetch main route
function home(){
    fetch("https://gully.herokuapp.com/api/v1", {
        method: "GET",
        headers:{
            "Content-Type":"application/json"
        }
    })
    .then((response) => response.json())
    .then((data)=>{
        document.getElementById("output").innerHTML = data["message"]
    })
    .catch((err) => console.log(err))
}