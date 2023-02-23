
var buttons = document.getElementsByClassName("myButton");

for (var i = 0; i < buttons.length; i++) {
  var button = buttons[i];
  button.originalColor = button.style.backgroundColor; // store the button's original color
}

function changeColor(button) {
  if (button.style.backgroundColor === "gray") {
    button.style.backgroundColor = "white" // change back to original color
  } else {
    button.style.backgroundColor = "gray"; // change color when clicked
  }
}

const track = document.getElementById("image-track");

const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;

const handleOnUp = () => {
  track.dataset.mouseDownAt = "0";  
  track.dataset.prevPercentage = track.dataset.percentage;
}

const handleOnMove = e => {
  if(track.dataset.mouseDownAt === "0") return;
  
  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
        maxDelta = window.innerWidth / 2;
  
  const percentage = (mouseDelta / maxDelta) * -100,
        nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
        nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);
  
  track.dataset.percentage = nextPercentage;
  
  track.animate({
    transform: `translate(${nextPercentage}%, -50%)`
  }, { duration: 1200, fill: "forwards" });
  
  for(const image of track.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${100 + nextPercentage}% center`
    }, { duration: 1200, fill: "forwards" });
  }
}

/* -- Had to add extra lines for touch events -- */

window.onmousedown = e => handleOnDown(e);

window.ontouchstart = e => handleOnDown(e.touches[0]);

window.onmouseup = e => handleOnUp(e);

window.ontouchend = e => handleOnUp(e.touches[0]);

window.onmousemove = e => handleOnMove(e);

window.ontouchmove = e => handleOnMove(e.touches[0]);


var lastScrollTop = 0;
window.addEventListener('scroll', function() {
  var st = window.pageYOffset || document.documentElement.scrollTop;
  var parallaxText = document.querySelector('.parallax-text');

  if (st > lastScrollTop){
    // Scroll down
    parallaxText.classList.add('fade-out');
  } else {
    // Scroll up
    parallaxText.classList.remove('fade-out');
  }
  
  lastScrollTop = st <= 0 ? 0 : st;
});