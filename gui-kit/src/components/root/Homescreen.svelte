<script>
    import Statusbar from "../systems/Statusbar.svelte";
    import Dock from "../systems/Dock.svelte";
    import Applist from "../systems/Applist.svelte";
    import AppOverview from "../apps/AppOverview.svelte";
</script>

<style>
    body {
        background-color: var(--forestgreen);
        color: var(--cream);
    }
</style>

<body>
    <Statusbar/>
    <!-- <Dock/> -->
    <!-- <Applist/> -->
    <AppOverview/>
</body>