const cleardiv = document.querySelector("#headingFiltersMobile > div");
const wdth = cleardiv.clientWidth;  //checking width of apply filter and clear section div
//console.log(wdth);
let clearbtn = document.querySelector("#headingFiltersMobile > div > a");   //clear button to format accordingly
if (wdth > 287) {
    //console.log("true");
    clearbtn.classList.add("float-right");
}
else {
    clearbtn.classList.add("mt-2");
}

clearbtn.onclick = () => {
    // console.log("clicked!!!")
    let checkbx = document.getElementsByClassName("checkbox");
    for (let i = 0; i < checkbx.length; i++) {
        let inpt = checkbx[i].childNodes[0].childNodes[0];
        inpt.checked = false;
    }
}