function sendRequest(ledState) {
    fetch('/?led=' + ledState, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .catch(error => {
        console.error('Error: ', error);
    });
}

document.getElementById('led-on').addEventListener('click', function(event) {
    event.preventDefault();
    sendRequest('on'); 
});

document.getElementById('led-off').addEventListener('click', function(event) {
    event.preventDefault();
    sendRequest('off');
});