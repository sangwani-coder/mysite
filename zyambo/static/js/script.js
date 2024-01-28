// type bio
let i = 0;
const bio = "My life is a symphony of technology and music, blending code and chords in pursuit of dreams.As a software architect, I weave intricate solutions for businesses, bringing their visions to life with pixel - perfect precision.My passion for technology, fueled by a lifetime dream of performing music, pushes me to bridge the gap between logic and creativity.";



const lang = 'Python, js, C, MySQL';
const speed = 55;


function typeWriter() {
  if (i < bio.length) {
    if (bio.charAt(i - 1) === '.') {
      document.getElementById("bio").innerHTML += "<br>";
    }
    document.getElementById("bio").innerHTML += bio.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
function modify() {
  document.getElementById('hide').classList.add('ready');
}


/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}


function calculatePrice() {
  // Get selected values
  const content = document.getElementById("content").value;
  const appType = document.getElementById("app-type").value;
  const discount = parseFloat(document.getElementById("discount").value);

  // Perform price calculation based on your criteria
  // Replace the following with your own pricing logic
  let baseHours = 20
  let basePrice = 200; // current base price

  if (content === "premium") {
    baseHours *= 7; // Additional cost for premium content
  }

  if (appType === "mobile-ios") {
    basePrice += 250; // Additional cost for an iOS mobile app
  }

  if (appType === "mobile-android") {
    basePrice += 200; // Additional cost for an android mobile app
  }

  if (appType === "desktop") {
    basePrice += 200; // Additional cost for a desktop app
  }

  // Calculate the final price with the discount
  let finalPrice = baseHours * basePrice;

  if (!isNaN(discount) && discount > 0) {
    finalPrice = finalPrice - (finalPrice * discount / 100);
  }

  var formattedNumber = finalPrice.toLocaleString();

  // Display the result
  document.getElementById("price").textContent = `K${formattedNumber}`;
}

const paragraphs = document.querySelectorAll('.text-wrap p:not(:first-child)');
paragraphs.forEach(paragraph => {
  const heading = paragraph.previousElementSibling;
  heading.addEventListener('click', () => {
    paragraph.style.display = paragraph.style.display === 'none' ? 'block' : 'none';
  });
});
