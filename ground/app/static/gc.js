function make_command_endpoint(cmd_name) {
    function callback() {
        fetch('/api/serial', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'command': cmd_name
            })
        })
    }

    return callback
}

gc_reset = make_command_endpoint('reset')
gc_open_servo = make_command_endpoint('open_servo')
gc_close_servo = make_command_endpoint('close_servo')
gc_pass_servo = make_command_endpoint('close_servo')

setTimeout(function(){ location.reload(); }, 2000);
