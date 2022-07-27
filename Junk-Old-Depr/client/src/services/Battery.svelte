<style>
    .battery-container {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: auto;
    }
    .battery-box {
        width: 23px;
        height: 11px;
        background-color: white;
    }
    .battery-border{
        width: 21px;
        height: 9px;
        margin: auto;
        transform: translate(0%,10%);
        background-color: black;
    }
    .battery-fill{
        width: 20px;
        height: 8px;
        margin: auto;
        transform: translate(0%,7%);
        background-color: white;
    }
    .battery-cell{
        width:2px;
        height: 5px;
        background-color: white;
    }

</style>

<div class='battery-container'>
    <div class='battery-box'>
        <div class='battery-border'>
            <div class='battery-fill'>
            </div>
        </div>
    </div>
    <div class='battery-cell'>
    </div>
</div>