var prevScrollPos = window.pageYOffset;

window.onscroll = function(){
    var currentPos = window.pageYOffset;
    if(prevScrollPos > currentPos){
        // document.getElementsByClassName('header')[0].style.height = "-4.5rem";
        document.getElementsByTagName('header')[0].style.top = "0rem";
    }else{
        // document.getElementsByClassName('header')[0].style.height = "0rem";
        document.getElementsByTagName('header')[0].style.top = "-4.5rem";
    }
    prevScrollPos = currentPos;
    console.log(prevScrollPos);
}