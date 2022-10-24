// type bio
let i = 0;
const bio = "I am a full-stack software developer.\
I love to build software for schools.\
In my spare time I study about Human Computer Interaction, Physics and History.\
My life motto is AIM HIGH.";

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