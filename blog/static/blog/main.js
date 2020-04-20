
function playSound(word) {
    let ctrl = document.getElementsByClassName(word);    
    ctrl[0].load()
    ctrl[0].play()
};

function scroller(){
    console.log(entryDiv.offsetTop)
    //entryDiv.style.top = '22px';
    //entryDiv.scrollIntoView();
}

let searchButt = document.getElementById('search-field-btn');
let searchField = document.getElementById('search-field');
let searchWord = searchField.textContent;
let entryDiv = document.getElementById(searchWord.trim());
let topPos = entryDiv.offsetTop;
let containerDiv = document.getElementById('word-container');

searchButt.addEventListener('click', scroller)

let elements = document.getElementsByClassName("soundButt");

let myFunction = function() {
    var attribute = this.getAttribute("data-sound");
    console.log(attribute)
    playSound(attribute)
};

Array.from(elements).forEach(function(element) {
    element.addEventListener('click', myFunction);
  });

