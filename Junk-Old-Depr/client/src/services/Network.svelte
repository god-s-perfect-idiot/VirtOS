
<style>
   #signal-strength {
    height: 15px;
    list-style: none;
    overflow: hidden;
    margin: 0;
    padding-left: 5px;
    }
    #signal-strength li {
    display: inline-block;
    width: 2.5px;
    float: left;
    height: 100%;
    margin-right: 1px;
    }
    #signal-strength li.pretty-strong {
    padding-top: 0px;
    }
    #signal-strength li.strong {
    padding-top: 3px;
    }
    #signal-strength li.weak {
    padding-top: 6px;
    }
    #signal-strength li.very-weak {
    padding-top: 9px;
    }
    #signal-strength li.dead {
    padding-top: 12px;
    }
    #signal-strength li div {
    height: 100%;
    background: white;
    }

</style>

<ul id="signal-strength">
    <li class="dead"><div></div></li>
    <li class="very-weak"><div></div></li>
    <li class="weak"><div></div></li>
    <li class="strong"><div></div></li>
    <li class="pretty-strong"><div></div></li>
</ul>
