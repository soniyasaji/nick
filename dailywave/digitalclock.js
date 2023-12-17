<div class="hero">
<div class="container">
    <div class="clock">
        <span id="hrs">00</span>
        <span>:</span>
        <span id="min">00</span>
        <span>:</span>
        <span id="sec">00</span>
    </div>
</div>
</div>
<script>
    let hrs = document.getElementById("hrs")
    let mins = document.getElementById("mins")
    let sec = document.getElementById("sec")

    setInteval(()=>{
    let currentTime = new Date();
    hrs.innerHTML = currentTime.getHours()<10?"0":"") + currentTime.getHours();
    min.innerHTML = currentTime.getMinutes()<10?"0":"") + currentTime.getMinutes();
    sec.innerHTML = currentTime.getSeconds()<10?"0":"") + currentTime.getSeconds();
    },1000)

console.log("digitalclock.js is connected")
</script>