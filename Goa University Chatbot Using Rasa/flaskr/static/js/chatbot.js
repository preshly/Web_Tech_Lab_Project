function loadDoc() {
    var fields = $( ":input" ).serializeArray();

    $( "#results" ).empty();
    jQuery.each( fields, function( i, field ) {
      //$( "#results" ).append( field.value + " " );
      $.post( "/result", {
    javascript_data: field.value+" "
});
    });
    refreshMessages();
    // TODO: The rest of the code will go here...
}


function refreshMessages() {
    $.ajax({
      url: 'chat.php',
      type: 'GET',
      dataType: 'html',
      success: function(data) {
        $('#chat').html(data); // data came back ok, so display it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              $('#chat').html(data); // data came back ok, so display it
      },
      error: function() {
        $('#chat').prepend('Error retrieving new messages..');
      }
    });
  }
  