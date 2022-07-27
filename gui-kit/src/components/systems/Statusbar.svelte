<script>
    $: time = (new Date()).toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
</script>

<style>
    .status-bar{
        margin-left: 2rem;
        margin-right: 2rem;
        height: 4rem;
        border-bottom: 1px solid #FFFDD0;
    }
    .time {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 4rem;
        font-size: 2.5rem;
        margin-left: 3rem;
        font-weight: 500;
    }
</style>

<div class="status-bar">
    <table>
        <tr>
            <td>
                <div class="time">
                    {time}
                </div>
            </td>
        </tr>
    </table>
</div>