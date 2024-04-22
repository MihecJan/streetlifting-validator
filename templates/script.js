const socket = io();

socket.on('Update_measurements', (measurements) => {
    const measurementList = document.getElementById("measurement_list");
    measurementList.innerHTML = "";

    measurements.forEach(measurement => {
        const listItem = document.createElement("li");
        listItem.textContent = JSON.stringify(measurement);
        measurementList.appendChild(listItem);
    });
});