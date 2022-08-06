<script>
    import {current} from '../_storage/store';

    const homeScreen = () => {
        $current = "sys:home";
    }

    $: time = (new Date()).toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
</script>

<style>
    .status-bar{
        display: flex;
        align-items: center;
        margin-left: 2rem;
        margin-right: 2rem;
        height: 4rem;
        border-bottom: 1px solid #FFFDD0;
    }
    .time {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 4rem;
        width: 15rem;
        font-size: 2.5rem;
        margin-left: 3rem;
        font-weight: 500;
    }
    .home {
        font-size: 3rem;
        color: var(--cream);
        text-align: end;
        width: 100%;
    }
</style>

<div class="status-bar">
    <div class="time">
        {time}
    </div>
    <div class="home">
        <ion-icon name="walk-outline" on:click={homeScreen}></ion-icon>
    </div>
</div>