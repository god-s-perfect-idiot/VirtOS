<script>
    import {current} from '../_storage/store';
    const viewApps = () => {
        $current = 'sys:applist';
    }
</script>

<style>
    .dock ion-icon {
        font-size: 6rem;
        display: flex;
        justify-content: center;
        width: 100%;
        position: absolute;
        bottom: 0%;
        margin-bottom: 2rem;
    }
</style>

<div class="dock"> 
    <ion-icon name="chevron-up-outline" on:click={viewApps}></ion-icon>
</div>