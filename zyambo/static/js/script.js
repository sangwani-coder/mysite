// type bio
let i = 0;
const bio = "Passionate software engineer, martial arts enthusiast, and a dedicated music teacher.\
My Tech Stack: \
C, Python, Typescript/Nodejs, Java, Lua, JavaScript, REST APIs, Bash, SQL, OOP.\
My Martial art styles: \
Kung-fu, Kyokoshin Karate, Kickboxing, Capoeira.\
My Music Instruments: \
Piano, Trumpet, Guitar.\
Certified Private Investigator";

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