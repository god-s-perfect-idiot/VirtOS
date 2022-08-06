<script>
    import {current} from '../_storage/store';
    const homeScreen = () => {
        $current = 'sys:home';
    }
    const launchApp = (app) => {
        $current = app;
    }
</script>

<style>
    .applist {
        margin-top: 3rem;
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .app-icon {
        height: 8rem;
        width: 8rem;
        border: 2px solid white;
        margin-top: 2rem;
        margin-left: 2rem;
        margin-right: 2rem;
        margin-bottom: 0.5rem;
        font-size: 4.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        border-top-right-radius:2.5rem;
        border-bottom-left-radius:2.5rem;
    }
    .app-text {
        display: flex;
        justify-content: center;
        font-size: 2.2rem;
        width: 12rem;
        max-width: 12rem;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }
    .applist-controls {
        width: 100%;
        height: 5rem;
        font-size: 4rem;
        display: flex;
        justify-content: left;
    }
</style>

<div class="applist">
    <table>
        <!-- 5 apps per row -->
        <tr>
            <td>
                <div class="applist-controls">
                    <ion-icon name="arrow-back-outline" on:click={homeScreen}></ion-icon>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <div class="app-icon" on:click={()=> launchApp('app:browser')}>
                    <ion-icon name="earth-outline"></ion-icon>
                </div>
                <div class="app-text">Browser</div>
            </td>
            <td>
                <div class="app-icon" on:click={()=> launchApp('app:clock')}>
                    <ion-icon name="time-outline"></ion-icon>
                </div>
                <div class="app-text">Clock</div>
            </td>
            <td>
                <div class="app-icon" on:click={()=> launchApp('app:stopwatch')}>
                    <ion-icon name="stopwatch-outline"></ion-icon>
                </div>
                <div class="app-text">StopWatch</div>
            </td>
            <td>
                <div class="app-icon">
                </div>
                <div class="app-text">Text</div>
            </td>
            <td>
                <div class="app-icon">
                </div>
                <div class="app-text">Text</div>
            </td>
        </tr>
    </table>
</div>