<script>
    import Statusbar from "../systems/Statusbar.svelte";
    import Dock from "../systems/Dock.svelte";
    import Applist from "../systems/Applist.svelte";
    import AppOverview from "../apps/AppOverview.svelte";
    import {current} from "../_storage/store";
</script>

<style>
    body {
        background-color: var(--forestgreen);
        color: var(--cream);
    }
</style>

<body>
    <Statusbar/>
    {#if $current === "sys:home"}
        <Dock/>
    {:else if $current === "sys:applist"}
        <Applist/>
    {:else}
        <AppOverview/>
    {/if}
</body>