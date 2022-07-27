<style>
    .clock {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .time-slot {
        margin-top: 20rem;
        font-size: 8rem;
        height: 10rem;
    }
    .date-slot {
        margin-top: 3rem;
        font-size: 5rem;
    }
    .day-slot {
        margin-top: 1rem;
        font-size: 4rem;
    }
</style>

<script>
    $: time = (new Date()).toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    $: date = new Date().toISOString().slice(0, 10);
    $: day = moment().format("dddd");
</script>

<div class="clock">
    <div>
        <div class="time-slot">
            {time}
        </div>
        <div class="date-slot">
            {date}
        </div>
        <div class="day-slot">
            {day}
        </div>
    </div>
</div>