<script>
    import Clock from '../../services/Clock.svelte'
    import Battery from '../../services/Battery.svelte'
    import Network from '../../services/Network.svelte'
    import WiFi from '../../services/WiFi.svelte'
</script>

<style>
    @font-face{
        font-family: 'SegoeWP';
        src: url('/SegoeWP.ttf')
    }
    .status-bar {
        display: table;
        font-family: 'SegoeWP';
        table-layout: auto;
        background-color: black;
        width: 100%;
        position: fixed;
        top: 0;
    }
    .clock {
        widows: 50px;
        text-align: right;
        padding-right: 5%;
        width: 7%;
        font-size: medium;
        
    }
    .battery {
        padding-left: 3%;
        padding-right: 3%;
        width: 7%;
    }
</style>

<table class='status-bar'>
    <tr>
        <td>
            <Network/>
        </td>
        <td></td>
        <td></td>
        <td></td>
        <td>
            <WiFi/>
        </td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td class='battery'>
            <Battery/>
        </td>
        <td class='clock'>
            <Clock/>
        </td>
    </tr>
</table>