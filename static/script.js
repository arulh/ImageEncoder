document.getElementById('submit_button').onclick = function() {
    console.log("button clicked");
    var tag = document.createElement("p");
    var text = document.createTextNode("Your photo is being processed. Please wait about 30 seconds.");
    tag.appendChild(text);
    var element = document.getElementById("main")
    element.appendChild(tag)
};