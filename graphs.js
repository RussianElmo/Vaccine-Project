function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState===4 && this.status ===200) {
        callback(this.response);
        }
    }
    request.open('get', path);
    request.send();
}


function ajaxPostRequest(path, j, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState===4 && this.status ===200) {
            callback(this.response);
        }
    }
    request.open("POST", path);
    request.send(j);
}


function showbar(response){
    let data = JSON.parse(response);
    var chartData = [
        {
            x: data[0],
            y: data[1],
            type: 'bar'

        }
    ];

    var layout = {
            title: {
                text: 'Fully Vaccinated by Location'
            },
            xaxis: {
                title: {
                    text: 'Location'
                }
            },
            yaxis: {
                title: {
                    text: '% Fully Vaccinated'
                }
            } 
    };

    Plotly.newPlot('bar', chartData, layout);
}


function showpie(reponse){
    let data = JSON.parse(reponse)

    var chartData = [
        {
            values: data,
            labels: ['Janssen', 'Moderna', 'Pfizer', 'Unknown'],
            type: 'pie'
        }
    ];

    var layout = {
        title: 'Vaccine Manufacturer Market Share'
    };

    Plotly.newPlot('pie', chartData, layout)
}



function sendData() {
    var input = JSON.stringify(document.getElementById('in').value.toUpperCase());
    ajaxPostRequest('/vacByDate', input, showline);
}


function showline(response) {
    let data = JSON.parse(response);
    
    var trace1 = 
    {
        x: data[1],
        y: data[0],
        type: 'scatter'
    };

    var layout =
    {
        title: '% of ' + document.getElementById('in').value.toUpperCase() + ' Fully Vaccinated By Date',
        xaxis: {
            title: 'Date'
        },
        yaxis: {
            title: '% Fully Vaccinated'
        }
    };

    var output = [trace1]
    Plotly.newPlot('line', output, layout);
}

ajaxGetRequest('/bar', showbar);
ajaxGetRequest('/pie', showpie);
