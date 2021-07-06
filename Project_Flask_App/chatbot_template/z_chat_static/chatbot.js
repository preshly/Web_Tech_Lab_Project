
$(document).ready(function () {
    //Toggle fullscreen
    $(".chat-bot-icon").click(function (e) {
        $(this).children('svg').toggleClass('animate');
        $('.chat-screen').toggleClass('show-chat');
    });
    
});

var userMessages = [];
var botMessages = [];


if (sessionStorage.count) {
    for (let i = 0; i <= Number(sessionStorage.count); i++) {
        $("#chatbox").innerHTML = sessionStorage.getItem(i)
    }
}


function buttonAction(button){
    var button_msg = button.innerHTML;
    getBotReply(button_msg)
}

function sendMessage(){
    var inp_msg = $('#input_msg').val();
    getBotReply(inp_msg)
}

function getBotReply(input) {
    // var inp_msg = $('#input_msg').val();
    var userHtml = chatBubble('me',input);
    $("#input_msg").val("");
    $("#chatbox").append(userHtml);

    userMessages.push(userHtml);

    $.get("/get", { msg: input }, function (data) {

        var botHtml = chatBubble('you',data);

        $("#chatbox").append(botHtml);
        botMessages.push(botHtml);

        if (sessionStorage.count) {
            sessionStorage.count = Number(sessionStorage.count) + 1;
        }
        else {
            sessionStorage.count = 0;
        }

        sessionStorage.setItem(sessionStorage.count, userHtml);
        sessionStorage.count = Number(sessionStorage.count) + 1;

        sessionStorage.setItem(sessionStorage.count, botHtml);

        $('#scroll').scrollTop((Number(sessionStorage.count) * 2) * 1000);

    });

}

function chatBubble(type,data){
    let el_p = document.createElement('p');
    el_p.classList.add("chat-bubble");
    el_p.classList.add(type);

    let el_span = document.createElement('span');
    el_span.innerHTML = data;

    $(el_span).find('button').addClass('btn btn-info custom');
    el_p.append(el_span);

    return el_p;
}

$("#send_button").click(sendMessage);

$("#input_msg").keypress(function (e) {

    if (e.which == 13) {
        sendMessage();
    }

});

