<script>
    //import ForceFullScreen from '../services/ForceFullScreen.svelte'
    import StatusBar from './widgets/StatusBar.svelte'
    import MetroGrid from './widgets/MetroGrid.svelte'
    import NavBar from './widgets/NavBar.svelte'
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

<div class='ui-black'>
    <StatusBar/>
    <MetroGrid/>
    <NavBar/>
</div>
<!-- <ForceFullScreen/> -->