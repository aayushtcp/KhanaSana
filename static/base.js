const hamm= document.querySelector('.hamburger');
const navigation_header= document.querySelector('.header');



const toogleNavbar = ()=>{
    navigation_header.classList.toggle("active");
}
hamm.addEventListener("click", ()=>toogleNavbar());