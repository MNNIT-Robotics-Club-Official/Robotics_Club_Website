let clearbtn = document.querySelector("#headingFiltersMobile > div > a");   //clear button to format accordingly

function formatBtn() {
    const cleardiv = document.querySelector("#headingFiltersMobile > div");
    const wdth = cleardiv.clientWidth;  //checking width of apply filter and clear section div
    //console.log(wdth);
    if (wdth > 287) {
        //console.log("true");
        clearbtn.classList.add("float-right");
        clearbtn.classList.remove("mt-2");
    }
    else {
        clearbtn.classList.add("mt-2");
        clearbtn.classList.remove("float-right");
    }
}

formatBtn();    //initial format

window.onresize = () => {
    formatBtn();
}

clearbtn.onclick = () => {
    // console.log("clicked!!!")
    let checkbx = document.getElementsByClassName("checkbox");
    for (let i = 0; i < checkbx.length; i++) {
        let inpt = checkbx[i].childNodes[0].childNodes[0];
        inpt.checked = false;
    }
}