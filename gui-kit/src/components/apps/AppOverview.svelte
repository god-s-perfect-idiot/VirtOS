<script>
    import Clock from "./Clock.svelte";
    import Stopwatch from "./Stopwatch.svelte";
    import Browser from "./Browser.svelte";
    import {current} from "../_storage/store.js";
</script>

<style>
    .overview {
        height: 100%;
        width: 100%;
    }
</style>

<div class="overview">
    {#if $current === "app:browser"}
        <Browser/>
    {:else if $current === "app:stopwatch"}
        <Stopwatch/>
    {:else if $current === "app:clock"}
        <Clock/>
    {/if}
</div>