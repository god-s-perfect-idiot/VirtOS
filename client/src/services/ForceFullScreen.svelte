<script>
    import { onMount } from 'svelte';
    import Fullscreen from 'svelte-fullscreen';
    
    onMount( async ()=> {
        document.getElementById("FullScreen").click();
    })
    
    
</script>
<Fullscreen let:onRequest >
    <button id="FullScreen" on:click="{()=>onRequest()}">asd</button>    

</Fullscreen>