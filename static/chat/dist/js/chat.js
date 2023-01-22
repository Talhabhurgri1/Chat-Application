
var loc = window.location
var wsStart = "ws://"
if (loc.protocol === "https") {
    wsStart = "wss://"
}
var endpoint = wsStart + loc.host + loc.pathname  // gives the endpoint 
console.log(endpoint)
var socket = new WebSocket(endpoint)

socket.onopen = async function (e) {
    console.log('open', e)
    $(".send").on('click', function (e) {
        e.preventDefault()
        var send_msg = $("#type_msg").val()
        // console.log("inside open")
        var data = {
            'message': send_msg
        }
        data = JSON.stringify(data)
        socket.send(data)
    })
}

socket.onmessage = async function (e) {
    console.log('message', e)
    var data = JSON.parse(e.data)
    var message = data['message']
    new_msg(message)
}

socket.onerror = async function (e) {
    console.log('error', e)
}

socket.onclose = async function (e) {
    console.log('close', e)
}

var msg_body = $(".new_chat") // Message body where chat will be appended
function new_msg(new_message) {
    msg = `<div class="message">
				<img class="avatar-md" src="dist/img/avatars/avatar-female-5.jpg"
					data-toggle="tooltip" data-placement="top" title="Keith" alt="avatar">
				<div class="text-main">
					<div class="text-group">
						<div class="text">
							<p>${new_message}</p>
						</div>
					</div>
					<span>09:46 AM</span>
				</div>
			</div>`
    msg_body.append(msg)
    msg_body.animate({
        scrollTop: $(document).height()
    }, 100)
}
