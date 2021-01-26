<script>
    import FullScreen from 'svelte-fullscreen'
</script>

<FullScreen let:onRequest>
    <div>
        <button on:load={() => onRequest()}>FullScreen</button>
    </div>
</FullScreen>