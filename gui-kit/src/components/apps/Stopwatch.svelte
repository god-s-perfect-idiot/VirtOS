<style>
    .stopwatch {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .counter {
        margin-top: 20rem;
        font-size: 5rem;
        height: 10rem;
    }
    .controls {
        margin-top: 3rem;
        font-size: 5rem;
        display: flex;
        justify-content: center;
    }
</style>

<script>
    import ButtonAlpha from '../ui-kit/ButtonAlpha.svelte';

    $: counter = 0;
    let runner = () => {
        counter++;
    };
    let runnerId;
    let active = false;

    const format = (s) => {
        const ms = s % 100;
        s = (s - ms) / 100;
        const secs = s % 60;
        s = (s - secs) / 60;
        const mins = s % 60;
        const hrs = (s - mins) / 60;
        return hrs + ':' + mins + ':' + secs + '.' + ms;
    }

    const start = () => {
        active = true;
        runnerId = setInterval(runner, 10);
    }

    const stop = () => {
        active = false;
        clearInterval(runnerId);
    }

    const reset = () => {
        counter = 0;
    }

</script>

<div class="stopwatch">
    <table>
        <tr>
            <div class="counter">
                {format(counter)}
            </div>
        </tr>
        <tr>
            <div class="controls">
                {#if !active}
                    <ButtonAlpha
                        width="8rem"
                        height="8rem"
                        inverted=true
                        spacing=2
                        on:click = {start}
                    >
                        <ion-icon name="play-outline"></ion-icon>
                    </ButtonAlpha>
                {:else}
                    <ButtonAlpha
                        width="8rem"
                        height="8rem"
                        inverted=true
                        spacing=2
                        on:click = {stop}
                    >
                        <ion-icon name="pause-circle-outline"></ion-icon>
                    </ButtonAlpha>
                {/if}
                <ButtonAlpha
                    width="8rem"
                    height="8rem"
                    inverted=true
                    spacing=2
                    on:click = {reset}
                >
                    <ion-icon name="refresh-outline"></ion-icon>
                </ButtonAlpha>
            </div>
        </tr>
    </table>
</div>