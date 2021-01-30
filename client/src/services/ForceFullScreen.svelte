<script>
    import Fullscreen from 'svelte-fullscreen'
</script>

<Fullscreen let:onRequest let:onExit>
    <div>
      <button on:click={() => onRequest()}>FullScreen</button>
      <button on:click={() => onExit()}>Screen</button>
    </div>
  </Fullscreen>