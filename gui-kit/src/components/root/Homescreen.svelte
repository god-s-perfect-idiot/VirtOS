<script>
    import Statusbar from "../systems/Statusbar.svelte";
    import Dock from "../systems/Dock.svelte";
    import Applist from "../systems/Applist.svelte";
    import AppOverview from "../apps/AppOverview.svelte";
</script>

<style>
    body {
        background-color: #021702;
        color: #FFFDD0;
    }
</style>

<body>
    <Statusbar/>
    <!-- <Dock/> -->
    <!-- <Applist/> -->
    <AppOverview/>
</body>