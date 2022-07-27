<script>
    //import ForceFullScreen from '../services/ForceFullScreen.svelte'
    import StatusBar from './widgets/StatusBar.svelte'
    import MetroGrid from './widgets/MetroGrid.svelte'
    import NavBar from './widgets/NavBar.svelte'
    import AppList from './widgets/AppList.svelte'

    import { handleGesture } from '../services/SwipeDetect.svelte';
    
    import { onMount } from 'svelte'
    import { slide, fly } from 'svelte/transition'

    let touchstartX = 0;
    let touchstartY = 0;
    let touchendX = 0;
    let touchendY = 0;

    let content = "homescreen";

    onMount(() => {
        const gestureZone = document.getElementById('main');
        gestureZone.addEventListener('touchstart', function(event) {
            touchstartX = event.changedTouches[0].screenX;
            touchstartY = event.changedTouches[0].screenY;
        }, false);

        gestureZone.addEventListener('touchend', function(event) {
            touchendX = event.changedTouches[0].screenX;
            touchendY = event.changedTouches[0].screenY;
            const direction = handleGesture(touchstartX, touchstartY, touchendX, touchendY)
            if(['left', 'right'].includes(direction)){
                if(direction === 'left') content='apps'
                else content='homescreen'
            }
        }, false); 
    })



</script>

<style>
    .ui-black {
        background-color: black;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
        width: 100%;
        height: 100%;
    }
</style>

<div class='ui-black' onscroll="switch_list()" id='main'>
    <StatusBar/>
    {#if content === 'homescreen'} 
        <MetroGrid/>
    {:else if content === 'apps'}
        <AppList/>
    {/if}
    <NavBar/>
</div>
<!-- <ForceFullScreen/> -->