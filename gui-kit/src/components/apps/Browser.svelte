<style>
    .address-bar {
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px solid var(--cream);
        height: 5rem;
        margin-left: 2rem;
        margin-right: 2rem;
        width: 80%;
        font-size: 3rem;
        padding-left: 1.5rem;
    } 
    .address-bar input {
        width: auto;
        height: 5rem;
        background: transparent;
        border: 0;
        margin: 0;
        color: var(--cream);
        outline: none;
    }
    .browser {
        width: 100%;
        height: 100%;
    }
    .goto {
        font-size: 4rem;
        height: 100%;
    }
    .tool-bar {
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 7rem;
    }
    .website {
        margin-top: 0.5rem;
        height: calc(100% - 14rem);
        background-color: var(--cream);
    }
    .force-mobile {
        width: 100%;
        max-width: 100%;
        height: 100%;
        margin: 0 auto;
        border-style: none;
        border-color: inherit;
        border-width: 0px;
        display: block;
    }
</style>

<script>
    let url="https://www.bing.com";
    const search = () => {
        const site = document.getElementById('site_address').value;
        url = site || url;
    }
</script>

<div class="browser">
    <div class="tool-bar">
        <div class='address-bar'>
            <ion-icon style="height: 100%;" name="refresh-outline" on:click={search}></ion-icon>
            <input id="site_address" type="text">
        </div>
        <div class="goto"> 
            <ion-icon style="height: 100%;" name="arrow-forward-outline" on:click={search}></ion-icon>
        </div>
    </div>
    <div class="website">
        <iframe class="force-mobile" src={url} title="search" noborder="0" scrolling="yes" seamless>
        </iframe>
    </div>
</div>