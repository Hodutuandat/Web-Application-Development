function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");
    document.getElementById("clock").innerText = `${hours}:${minutes}:${seconds}`;
}

setInterval(updateClock, 1000);
updateClock();