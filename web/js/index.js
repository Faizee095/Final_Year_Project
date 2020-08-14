async function submitDetails() {
    user_name = document.getElementById("name").value;
    email_id = document.getElementById("email").value;
    password = document.getElementById("password").value;
    music_path = document.getElementById("music_path").value;
    // get_user_details(user_name);

    return_value = await eel.get_user_details(user_name, email_id, password, music_path)();
    document.getElementById("message").innerHTML = return_value;
    hide();

}

eel.expose(start_listening);
function start_listening() {
    window.alert("received")
    document.getElementById("message").innerHTML = "Started listening . . . ";
}

eel.expose(stop_listening);
function stop_listening() {
    document.getElementById("message").innerHTML = "Stopped listening . . . ";
}

function hide() {
    var x = document.getElementById("message");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function kickStart() {
    hide();
    //eel.kickstart_console();
}

async function startVOIP() {
    isChecked = document.getElementById("power").checked;
    console.log("value here in startVOIP ", isChecked)
    if (isChecked == true) {
        eel.voip()
        console.log("started ")
    } else {
        console.log("trying to stop")
        eel.stop_voip()
    }

}