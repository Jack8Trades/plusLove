// Grab image and button elements from HTML document
var pickUpLine = document.querySelector("#pickUpLine");
var btn = document.querySelector("#rand_btn");

// Asynchronous function that gets data from external API
async function generateImage() {
    var response = await fetch("http://yesno.wtf/api/");
    var data = await response.json();
    var answer = data.answer;
    console.log(data.answer);

    document.querySelector("#pickUpLine").innerHTML = answer;

    pickUpLine = answer;



}
// Add event listener to button to call 'generateImage'function when pressed
btn.addEventListener('click', generateImage);