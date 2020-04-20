var word = document.getElementById('word'),
    ctrl = document.getElementById('audioControl');

ctrl.onclick = function () {
    word.play()
    return false;

};