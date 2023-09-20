// type bio
let i = 0;
const bio = "I specialize in crafting custom software solutions that drive businesses forward.\
With a deep passion for technology and a keen eye for detail, I have successfully delivered results for clients across various industries.\
Are you ready to transform your ideas into powerful, user-friendly software solutions? Look no further.\
Click the Get Your Cost Estimate button to request a free quote.";



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
  let basePrice = 6950; // current base price

  if (content === "premium") {
    basePrice *= 2.5; // Additional cost for premium content
  }

  if (appType === "mobile-ios") {
    basePrice += 9550; // Additional cost for an iOS mobile app
  }
  
  if (appType === "mobile-android") {
    basePrice += 8550; // Additional cost for an android mobile app
  }
  
  if (appType === "mobile-both") {
    basePrice += 13000; // Additional cost for an iOS and android mobile app
  }
  
  if (appType === "desktop") {
    basePrice += 12550; // Additional cost for a desktop app
  }

  // Calculate the final price with the discount
  let finalPrice = basePrice;

  if (!isNaN(discount) && discount > 0) {
    finalPrice = basePrice - (basePrice * discount / 100);
  }

  var formattedNumber = finalPrice.toLocaleString();

  // Display the result
  document.getElementById("price").textContent = `K${formattedNumber}`;
}
