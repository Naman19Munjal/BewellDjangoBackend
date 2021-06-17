let speech = new SpeechSynthesisUtterance();
speech.lang = "en";

const container = document.getElementById('container');
const text = document.getElementById('text');

var appendmin = document.getElementById('minutes');
var appendsec = document.getElementById('seconds');
var sec = 00;
var min = 00;

const totalTime = 7500;
const breatheTime = (totalTime / 5) * 2;
const holdTime = totalTime / 5;



function breathAnimation() {
    text.innerText = 'Breathe In!';
    container.className = 'container grow';
    speech.text = "Breathe In";
    window.speechSynthesis.speak(speech);

    setTimeout(() => {
        text.innerText = 'Hold!';
        speech.text = "Hold";
        window.speechSynthesis.speak(speech);

        setTimeout(() => {
            text.innerText = 'Breathe Out!';
            container.className = 'container shrink';
            speech.text = "Breathe Out";
            window.speechSynthesis.speak(speech);
        }, holdTime);
    }, breatheTime);
}

function startTimer() {
    sec++;

    if (sec <= 9) {
        appendsec.innerHTML = "0" + sec;
    }

    if (sec > 9) {
        appendsec.innerHTML = sec;

    }

    if (sec > 59) {
        console.log("seconds");
        min++;
        appendmin.innerHTML = "0" + min;
        sec = 0;
        appendsec.innerHTML = "0" + 0;
    }

    if (min > 9) {
        appendmin.innerHTML = min;
    }

}


var animationValue = null;
var Interval = null;

function start() {
    animationValue = setInterval(breathAnimation, totalTime);
    Interval = setInterval(startTimer, 1000);
}
function stop() {
    clearInterval(animationValue);
    clearInterval(Interval);
}
