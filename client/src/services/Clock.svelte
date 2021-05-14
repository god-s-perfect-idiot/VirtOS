<script>
    
    import {onMount} from 'svelte'

    let time = (new Date()).toLocaleTimeString()
    $: _time = time.substr(0, time.length-6)
    onMount(() => {
		const interval = setInterval(() => {
			time = (new Date()).toLocaleTimeString()
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>


<div>
    <span>
        {_time}
    </span>
</div>