// type bio
let i = 0;
const bio = "I have 3 years  experience in full-stack software development.\
A strong experience with the following languages: \
C, Python, Typescript/Nodejs, Java, Lua.\
A solid background in Object-oriented programming (OOP). Experience with Docker.\
Experience in algorithm design, data structures and writing unit tests. \
Database engine knowledge. Knowledge with Web Sockets, REST APIs.\
Cloud provider experience (AWS, Azure). Experience with development tools such as jira, git, bash.";

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