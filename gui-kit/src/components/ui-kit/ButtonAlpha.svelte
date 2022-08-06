<script>
    export let width;
    export let height;
    export let text="";
    export let inverted=false;
    export let spacing=0;
</script>

<style>
    .button-alpha {
        border-radius: 2rem;
        width: 10rem;
        height: 5rem;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .regular {
        border: 2px solid var(--cream);
    }
    .inverted {
        border: 2px solid var(--cream);
        background-color: var(--cream);
        color: var(--forestgreen);
    }
</style>

<div class="button-alpha {inverted ? "inverted" : "regular"}" style="width: {width}; height: {height}; margin-left:{spacing}rem; margin-right:{spacing}rem" on:click>
    {text || ''}
    <slot/>
</div>