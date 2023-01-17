
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

//  Alert message function 
function error_msg(msg, alert_type){
    var timer = 0 
    var form = $("#msg")
    var alert_msg  = `<div class="alert alert-${alert_type}" role="alert">
    ${msg}
  </div>
  `
  $("#signup").prop('disabled', true)
  form.html(alert_msg)
  setTimeout(function() { 
    $(".alert").hide();
    $("#signup").prop('disabled', false)

}, 5000);
}
