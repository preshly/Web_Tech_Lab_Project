
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
        $("#chatbox").append(sessionStorage.getItem(i));
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
    var userHtml = '<p class="chat-bubble me"><span>' + input + "</span></p>";
    $("#input_msg").val("");
    $("#chatbox").append(userHtml);

    userMessages.push(userHtml);

    $.get("/get", { msg: input }, function (data) {

        var botHtml = '<p class="chat-bubble you"><span>' + data + "</span></p>";

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

        $('#chatbox').scrollTop((Number(sessionStorage.count) * 2) * 100);

    });

}

$("#send_button").click(sendMessage);

$("#input_msg").keypress(function (e) {

    if (e.which == 13) {
        sendMessage();
    }

});
