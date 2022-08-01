// type bio
let i = 0;
const bio = 'My name is Peter Zyambo a software engineering student at ALX, specializing in backend engineering.\
I love solving problems and buid fullstack web and desktop applications.\
In my spare time I study about Human Computer Interaction (HCI) and Database Design.\
My motto in life is to AIM HIGH.';

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
    