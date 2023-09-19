// type bio
let i = 0;
const bio = "I specialize in crafting custom software solutions that drive businesses forward.\
With a deep passion for technology and a keen eye for detail, I have successfully delivered results for clients across various industries.\
Are you ready to transform your ideas into powerful, user-friendly software solutions? Look no further.\
Click the Get started button to request a free quote.";



const lang = 'Python, js, C, MySQL';
const speed = 55;


function typeWriter() { 
    if ( i < bio.length) {
        if ( bio.charAt(i-1) === '.'){
            document.getElementById("bio").innerHTML += "<br>";    
        }
        document.getElementById("bio").innerHTML += bio.charAt(i);
        i++;
        setTimeout(typeWriter , speed);
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