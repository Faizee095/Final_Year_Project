function lFunction() {
    document.getElementById("lnav").style.display = "none";
}
function rFunction() {
    document.getElementById("rnav").style.display = "none";
}

eel.expose(show_info);
function show_info(msg) {
    document.getElementById("information").innerHTML = msg;
    setTimeout(function () {
        document.getElementById("information").innerHTML = "";
    }, 3000);
    return
}