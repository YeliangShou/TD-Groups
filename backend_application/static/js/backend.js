function makeCall() {
  alert("ITS NOW");
  console.log("this is my key");
  console.log(localStorage.getItem("uid"));
  fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(response => response.json())
    .then(json => console.log(json));
}
